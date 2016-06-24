# encoding: utf-8
import os
from django.http import HttpResponse,HttpResponseRedirect  
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context
from django.shortcuts import render_to_response,render,get_object_or_404  
from django.contrib.auth.models import User  
from django.contrib import auth
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from bootstrap_toolkit.widgets import BootstrapUneditableInput 
from django.http import JsonResponse
from .models import CmVrmsBaselineErrors,CmVrmsBaselineProjects,CM_BaseLine_Data_Info,CM_BaseLine_Info,CM_BaseLine_Subject_Info,CmVrmsBaselineIssues,CmVrmsBaselineCustomValues,CmVrmsBaselineUsers,CmVrmsBaselineRequire,UpdatetimeInfo

from django.db.models import Avg, Max, Min, Count
from django.shortcuts import render_to_response
import MySQLdb
import datetime
import re
import time
from  fileupload.models import NamemapInfo,VerConfInfo,SystemInfo,convert_name
from django.db import connection,transaction
NAME_MAP = NamemapInfo().namemap_info
'''
NAME_MAP = {"本币":"本币交易系统",
            "外汇":"外汇交易系统",
            "IMIX中间件子系统":"IMIX",
            "[未立项]外汇交易系统":"外汇交易系统",
            "C-Swap":"C-Swap系统",
            "X-Swap":"X-Swap系统",
            "X-REPO":"X-Repo系统",
            "X-Repo":"X-Repo系统",
            "货币网UAT环境":"货币网"
            }
'''
# Create your views here.
CM_BaseLine_Data = CM_BaseLine_Data_Info()
baseline_info = CM_BaseLine_Data.base_line_info


def transfer_date(date_int):
    #输入20151029,返回new Date(2015,10,29)
    date_str = str(date_int)
    year,month,day = date_str[:4],date_str[4:6],date_str[6:]
    return "new Date({},{},{})".format(year,month,day)

def transfer_date_more(date_int):
    #输入20151029,返回new Date(2015,10,29)
    date_str = str(date_int)
    year,month,day = date_str[:4],date_str[4:6],date_str[6:]
    return "new Date({},{},{})".format(year,month,day)
    #return "new Date().setFullYear({},{},{})".format(year,month,day)
    #return "2015-12-30"
def tranfer_value(this_time_data):
    time_date = []
    for i in range(0,len(this_time_data)):
        tmp_val = this_time_data[i].replace(this_time_data[i][7:15],transfer_date_more(this_time_data[i][7:15]))
        time_date.append(tmp_val)
    return time_date
        
        

def cm_baseline(request):
    c = Context({'STATIC_URL': '/static/'})
    #need_date_time = datetime.date(2015,06,22)
    need_date_time = datetime.date.today()
    try:
        app_name_list,this_time_data,old_time_data,new_time_data = CM_BaseLine_Data.get_tri_datas(need_date_time)
        #{name : '本币系统-V1.2.3.1', value : 1.2, xAxis: 1, yAxis: -1.5}
        c['need_date_time'] = need_date_time #基线的基准时间
        c['app_name_list'] = app_name_list#所有系统名称

        this_time_data_val = [int(val.split(",")[0].split(":")[1]) for val in this_time_data]
        old_time_data_val = [int(val.split(",")[0].split(":")[1]) for val in old_time_data]
        new_time_data_val = [int(val.split(",")[0].split(":")[1]) for val in new_time_data]
        c["this_mark_point_info_list"] = ["{name : '"+app_name_list[i]+"|"+this_time_data[i].split(",")[1].split(":")[1].strip("'")+"', xAxis:'"+app_name_list[i]+"', yAxis: "+transfer_date(this_time_data_val[i])+"}" for i in range(0,len(app_name_list))]
        c["old_mark_point_info_list"] = ["{name : '"+app_name_list[i]+"|"+old_time_data[i].split(",")[1].split(":")[1].strip("'")+"',  xAxis:'"+app_name_list[i]+"', yAxis: "+transfer_date(old_time_data_val[i])+"}" for i in range(0,len(app_name_list))]
        c["new_mark_point_info_list"] = ["{name : '"+app_name_list[i]+"|"+new_time_data[i].split(",")[1].split(":")[1].strip("'")+"',  xAxis:'"+app_name_list[i]+"', yAxis: "+transfer_date(new_time_data_val[i])+"}" for i in range(0,len(app_name_list))]
        c['min_time'] = transfer_date(min(min(this_time_data_val),min(old_time_data_val),min(new_time_data_val)))
        c['max_time'] = transfer_date(max(max(this_time_data_val),max(old_time_data_val),max(new_time_data_val)))
        
        this_time_data = tranfer_value(this_time_data)
        old_time_data = tranfer_value(old_time_data)
        new_time_data = tranfer_value(new_time_data)
        
        c['baseline_info_list'] = this_time_data#记录y轴数值
        c['oldline_info_list'] = old_time_data#记录y轴数值
        c['newline_info_list'] = new_time_data#记录y轴数值        
    except:
        c["jump_to"] =  "version_node_detail"
        out_path = "cm_baseline"  
        return render_to_response(out_path+'.html',context_instance=c)
    c["jump_to"] =  "version_node_detail"
    out_path = "cm_baseline"  
    return render_to_response(out_path+'.html',context_instance=c)


def baseline_date_search(request):
    #按照搜索时间生成基线
    c = Context({'STATIC_URL': '/static/'})
    out_path = "cm_baseline"  
    str_need_date_time = request.GET["query"].encode("utf-8")#获取搜索框中的时间
    if not str_need_date_time.strip():
        return render_to_response(out_path+'.html',context_instance=c)
    try:
        need_date_time = datetime.datetime.strptime(str_need_date_time,'%m/%d/%Y').date()#将字符串转化为date型
        app_name_list,this_time_data,old_time_data,new_time_data = CM_BaseLine_Data.get_tri_datas(need_date_time)
        if len(app_name_list) > 0:
            c['need_date_time'] = need_date_time #基线的基准时间
            c['app_name_list'] = app_name_list#所有系统名称

            this_time_data_val = [int(val.split(",")[0].split(":")[1]) for val in this_time_data]
            old_time_data_val = [int(val.split(",")[0].split(":")[1]) for val in old_time_data]
            new_time_data_val = [int(val.split(",")[0].split(":")[1]) for val in new_time_data] 
            c["this_mark_point_info_list"] = ["{name : '"+app_name_list[i]+"|"+this_time_data[i].split(",")[1].split(":")[1].strip("'")+"', xAxis:'"+app_name_list[i]+"', yAxis: "+transfer_date(this_time_data_val[i])+"}" for i in range(0,len(app_name_list))]
            c["old_mark_point_info_list"] = ["{name : '"+app_name_list[i]+"|"+old_time_data[i].split(",")[1].split(":")[1].strip("'")+"',  xAxis:'"+app_name_list[i]+"', yAxis: "+transfer_date(old_time_data_val[i])+"}" for i in range(0,len(app_name_list))]
            c["new_mark_point_info_list"] = ["{name : '"+app_name_list[i]+"|"+new_time_data[i].split(",")[1].split(":")[1].strip("'")+"',  xAxis:'"+app_name_list[i]+"', yAxis: "+transfer_date(new_time_data_val[i])+"}" for i in range(0,len(app_name_list))]
            c['min_time'] = transfer_date(min(min(this_time_data_val),min(old_time_data_val),min(new_time_data_val)))
            c['max_time'] = transfer_date(max(max(this_time_data_val),max(old_time_data_val),max(new_time_data_val)))
            
            c["jump_to"] =  "version_node_detail"
            
            this_time_data = tranfer_value(this_time_data)
            old_time_data = tranfer_value(old_time_data)
            new_time_data = tranfer_value(new_time_data)            
            c['baseline_info_list'] = this_time_data#记录y轴数值
            c['oldline_info_list'] = old_time_data#记录y轴数值
            c['newline_info_list'] = new_time_data#记录y轴数值
                       
        
        return render_to_response(out_path+'.html',context_instance=c)
    except:#如果获取数据失败了(尤其是get_tri_datas那个函数)
        return render_to_response(out_path+'.html',context_instance=c)

def baseline_sysver_search(request):
    #按照搜索版本对应的升级时间生成基线
    out_path = "cm_baseline" 
    c = Context({'STATIC_URL': '/static/'})
    system_version = request.GET["query"].encode("utf-8")#获取搜索框中系统及版本
    if "V" not in system_version:
        return render_to_response(out_path+'.html',context_instance=c)
    sysname = system_version.split("V")[0]
    vernum = system_version.split("V")[1]
    version = "V"+vernum
    queryset = CM_BaseLine_Info.objects.filter(AppName=sysname ,AppVersion=version).values('UpdateDate')
    if not queryset:
        return render_to_response(out_path+'.html',context_instance=c)
    
    datestr = str(queryset[0]["UpdateDate"])
    need_date_time = datetime.datetime.strptime(datestr,'%Y-%m-%d').date()
    #need_date_time = datetime.date(2015,06,22)
    app_name_list,this_time_data,old_time_data,new_time_data = CM_BaseLine_Data.get_tri_datas(need_date_time)
    c['need_date_time'] = need_date_time #基线的基准时间
    c['app_name_list'] = app_name_list#所有系统名称
    c['baseline_info_list'] = this_time_data#记录y轴数值
    c['oldline_info_list'] = old_time_data#记录y轴数值
    c['newline_info_list'] = new_time_data#记录y轴数值
    this_time_data_val = [int(val.split(",")[0].split(":")[1]) for val in this_time_data]
    old_time_data_val = [int(val.split(",")[0].split(":")[1]) for val in old_time_data]
    new_time_data_val = [int(val.split(",")[0].split(":")[1]) for val in new_time_data]
    c["this_mark_point_info_list"] = ["{name : '"+app_name_list[i]+"|"+this_time_data[i].split(",")[1].split(":")[1].strip("'")+"', xAxis:'"+app_name_list[i]+"', yAxis: "+str(this_time_data_val[i])+"}" for i in range(0,len(app_name_list))]
    c["old_mark_point_info_list"] = ["{name : '"+app_name_list[i]+"|"+old_time_data[i].split(",")[1].split(":")[1].strip("'")+"',  xAxis:'"+app_name_list[i]+"', yAxis: "+str(old_time_data_val[i])+"}" for i in range(0,len(app_name_list))]
    c["new_mark_point_info_list"] = ["{name : '"+app_name_list[i]+"|"+new_time_data[i].split(",")[1].split(":")[1].strip("'")+"',  xAxis:'"+app_name_list[i]+"', yAxis: "+str(new_time_data_val[i])+"}" for i in range(0,len(app_name_list))]
    c['min_time'] = min(min(this_time_data_val),min(old_time_data_val),min(new_time_data_val))
    c['max_time'] = max(max(this_time_data_val),max(old_time_data_val),max(new_time_data_val))
    c["jump_to"] =  "version_node_detail"
     
    return render_to_response(out_path+'.html',context_instance=c)


def cm_baseline_count(request):
    c = Context({'STATIC_URL': '/static/'})
    out_path = "count_cm_baseline"  
    
    cursor1 = connection.cursor() 
    cursor1.execute("SELECT DATE_FORMAT(UpdateDate,'%Y-%m') months, AppName, COUNT(AppName) counts FROM cm_vrms_baseline_cm_baseline_info GROUP BY months ,AppName")
    raw_result = cursor1.fetchall()#month,系统名,当月升级次数
    sys_up_info_dict = {}#app_name,month,update_num
    for sys_up_info in raw_result:
        sys_month,app_name,update_num = sys_up_info
        if app_name not in sys_up_info_dict:
            sys_up_info_dict[app_name] = {}
        sys_up_info_dict[app_name][sys_month] = int(update_num)
    cursor2 = connection.cursor()
    cursor2.execute("SELECT DATE_FORMAT(UpdateDate,'%Y-%m') months FROM cm_vrms_baseline_cm_baseline_info GROUP BY months")
    raw_result_month = cursor2.fetchall()
    c['Updatemonth_list'] = [val[0] for val in raw_result_month]
    
    c['AppName_list'] = sys_up_info_dict.keys()#x轴上的系统名列表
    c['update_counts_list'] = [[sys_up_info_dict[app_name_val].get(month_val,0) for app_name_val in c['AppName_list']] for month_val in c['Updatemonth_list']]
    c['update_counts_list_1'] = c['update_counts_list'][0]#单独把第一行的数据拿出来
    c['update_counts_list'] = c['update_counts_list'][1:]
    c['update_month_1'] = c['Updatemonth_list'][0]
    c['update_month'] = c['Updatemonth_list'][1:]
    c['AppName_list'] = ["\\n"*(i%5)+c['AppName_list'][i] for i in range(len(c['AppName_list']))]#增加\n
    return render_to_response(out_path+'.html',context_instance=c)

def get_dict_map(info_map,info_set,info_key):
    """递归调用自身,返回由该根目录遍历而得的所有节点;输入为字典、已有list、根节点key"""
    tmp_set = info_map.get(info_key,set())
    info_set = info_set|tmp_set
    for info_key in tmp_set:
        info_set = info_set|get_dict_map(info_map,info_set,info_key)
    return info_set
        
def get_project_map():
    """获取所有映射到主项目群的project_id,产出 project-项目群名 的映射关系"""
    project_list = CmVrmsBaselineProjects.objects.all()#project的信息,获取应用到每个项目群的映射关系
    need_check_set = set([272,273,274,275,276,277,278,280,433,27,28,30,31,32,33,34,35,36])
    project_child = {}
    project_name = {}
    group_dict = {}#存放每个need_check_set对应的所有子id集合
    for info in project_list:
        id = info.id
        name = info.name
        parent_id = info.parent_id
        project_name[id] = name.encode("utf-8")
        if parent_id not in project_child:
            project_child[parent_id] = set()
        project_child[parent_id].add(id)#记录子节点，待会儿自上(项目群)而下遍历
    for id in need_check_set:
        tmp_set = set()
        need_set = get_dict_map(project_child,tmp_set,id)#给tmp_set赋值,包含该群下所有的子节点
        for child_id in need_set:
            group_dict[child_id] = project_name[id]
    return group_dict

def update_db_from_work(request):
    '''由issue表和conf表和user表,更新CM_BaseLine_Subject_Info表'''
    #{4:"工作类别",35:"开始时间",36:"计划完成时间",68:"升级类别",69:"补丁号",70:"升级前版本号",71:"发布版本号",72:"上线版本号",73:"升级审批人",74:"升级环境（一级）",75:"环境分类（二级）",76:"环境分类（三级）",77:"升级日期",78:"变更内容-部署升级",79:"升级方式",80:"是否有数据库变更",81:"客户端内容",82:"基线号",83:"升级步骤手册页数",88:"工作量（人天）",84:"问题原因",87:"问题分类-升级问题",229:"升级原因"}
    CM_BaseLine_Subject_Info.objects.all().delete()#首先全部删除该表
    CM_BaseLine_Info.objects.all().delete()#首先全部删除该表
    CmVrmsBaselineErrors.objects.all().delete()#首先全部删除该表  
    id_val_map = [4,35,36,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,88,84,87,229]
    issue_info_list = CmVrmsBaselineIssues.objects.all()#issue所有信息
    customvalues_list = CmVrmsBaselineCustomValues.objects.all()#issue_id,type_id,value的所有信息
    user_list = CmVrmsBaselineUsers.objects.all()#issue_id,type_id,value的所有信息
    group_dict = get_project_map()#映射字典,给定一个id,返回其对应的项目群
    
    
    issue_dict = {}
    custom_value_dict = {}
    user_dict = {}
    for issue_info in issue_info_list:
        id=issue_info.id
        subject=issue_info.subject.encode("utf-8")
        issue_dict[id] = [issue_info.id,subject,issue_info.assigned_to_id,issue_info.project_id,issue_info.status_id]
    for customvalue in customvalues_list:
        customized_id=customvalue.customized_id
        custom_field_id=customvalue.custom_field_id
        value = ""
        if customvalue.value:
            value=customvalue.value.encode("utf-8")
        if customized_id not in custom_value_dict:
            custom_value_dict[customized_id] = {}
        custom_value_dict[customized_id][custom_field_id] = value
    for user in user_list:
        user_dict[user.id]=user.lastname+user.firstname
    for issue_id in issue_dict:
        raw_id,subject,assigned_to_id,project_id,status_id = issue_dict[issue_id]
        issue_one = [subject]#一共22列,这是第一列
        issue_1 =raw_id
        issue_2 = status_id
        username=user_dict.get(assigned_to_id)
        groupname = group_dict.get(project_id,"未知")
        for type in id_val_map:
            type_value = custom_value_dict[issue_id].get(type,"")
            issue_one.append(type_value)
        issue_one.append(username)
        issue_one.append(groupname)
        subject_info_tmp = CM_BaseLine_Subject_Info(raw_id =issue_1,status_id=issue_2,subject = issue_one[0],work_type = issue_one[1],start_time = issue_one[2],
                                                    due_time = issue_one[3],update_type = issue_one[4],version_num = issue_one[5],
                                                    old_version_num = issue_one[6],publish_version_num = issue_one[7],online_version_num = issue_one[8],
                                                    approve_person = issue_one[9],environment_fir = issue_one[10],environment_sec = issue_one[11],
                                                    environment_thi = issue_one[12],update_date = issue_one[13],change_content = issue_one[14],
                                                    update_method = issue_one[15],db_changed = issue_one[16],client_content = issue_one[17],
                                                    base_line_num = issue_one[18],update_book_num = issue_one[19],work_num = issue_one[20],problem_source = issue_one[21],
                                                    problem_type = issue_one[22], update_reason =issue_one[23], author_name = issue_one[24], project = issue_one[25])
        subject_info_tmp.save()#插入     
        '''error数据表插入'''   
        if(len(issue_one[22])>0):#若存在问题
            base_error_tmp = CmVrmsBaselineErrors(raw_id =issue_1,status_id=issue_2,subject = issue_one[0],UpdateDate = issue_one[2],
                                                    author_name = issue_one[24], project = issue_one[25],
                                                    problem_type = issue_one[22], problem_source = issue_one[21])
        try:
            base_error_tmp.save()
        except:
            pass             
        
        '''base_info数据表插入'''   
        environment_fir = issue_one[10]
        update_type = issue_one[4]
        if ("V" not in subject) and ("v" not in subject):
            continue
        if ('UAT' not in environment_fir) and ('模拟' not in environment_fir):
            continue#这些情况不需要考虑
        if ('升级' not in update_type) and ('版本同步' not in update_type) and ('模拟发布' not in update_type):
            continue

        
        
        app_name = subject.split("V")[0].split("v")[0].strip()
        app_name = app_name.strip("\\")
        NAME_MAP = NamemapInfo().namemap_info
        
        if len(app_name) < 2:
            continue
        if app_name in NAME_MAP:
            app_name = NAME_MAP[app_name]
        publish_version_num_str = issue_one[7]#此处需要对版本进行验证
        version_matchs = re.findall(r"[\.\d]+",publish_version_num_str)
        publish_version_num = ""
        if len(version_matchs)>0:
            nums = version_matchs[0].split(".")
            if len(nums) == 2:
                nums.append("0")
            if len(nums) == 3:
                nums.append("0")
            if len(nums) == 4:
                publish_version_num = "V{}.{}.{}.{}".format(*nums)
            if len(nums)>4:
                nums = nums[0:4]
                publish_version_num = "V{}.{}.{}.{}".format(*nums)
        if publish_version_num == "":#如果版本号这一关不符合规范
            continue
        update_date = issue_one[13]
        base_line_num = issue_one[18]
        update_book_num = issue_one[19]
        work_num = issue_one[20]
        """
        base_info_tmp = CM_BaseLine_Info(AppName = app_name,AppVersion = publish_version_num,
                                         UpdateDate=update_date,BaseLine = base_line_num,
                                        PageNumber = update_book_num,UppradeTime = work_num,
                                        version_num = issue_one[5],environment_fir = issue_one[10],
                                        UpgradeMan = issue_one[23], project = issue_one[24],
                                        problem_type = issue_one[22], problem_source = issue_one[21])
        """
        base_info_tmp = CM_BaseLine_Info(raw_id =issue_1,status_id=issue_2,AppName = app_name,AppVersion = publish_version_num,
                                         UpdateDate=update_date,BaseLine = base_line_num,
                                        PageNumber = update_book_num,UppradeTime = work_num,
                                        version_num = issue_one[5],environment_fir = issue_one[10],
                                        UpgradeMan = issue_one[24], project = issue_one[25],update_reason = issue_one[23],
                                        problem_type = issue_one[22], problem_source = issue_one[21],update_type = issue_one[4])
        
        try:
            base_info_tmp.save()
        except:
            pass
        
       
                        
        
    return HttpResponseRedirect('/cm_baseline/')#重定向


def update_db_from_work_bi(request):
    '''由issue表和conf表和user表,更新CM_BaseLine_Subject_Info表'''
    #{4:"工作类别",35:"开始时间",36:"计划完成时间",68:"升级类别",69:"补丁号",70:"升级前版本号",71:"发布版本号",72:"上线版本号",73:"升级审批人",74:"升级环境（一级）",75:"环境分类（二级）",76:"环境分类（三级）",77:"升级日期",78:"变更内容-部署升级",79:"升级方式",80:"是否有数据库变更",81:"客户端内容",82:"基线号",83:"升级步骤手册页数",88:"工作量（人天）",84:"问题原因",87:"问题分类-升级问题",229:"升级原因"}
    CM_BaseLine_Subject_Info.objects.all().delete()#首先全部删除该表
    CM_BaseLine_Info.objects.all().delete()#首先全部删除该表
    CmVrmsBaselineErrors.objects.all().delete()#首先全部删除该表  
    id_val_map = [4,35,36,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,88,84,87,229]
    issue_info_list = CmVrmsBaselineIssues.objects.all()#issue所有信息
    customvalues_list = CmVrmsBaselineCustomValues.objects.all()#issue_id,type_id,value的所有信息
    user_list = CmVrmsBaselineUsers.objects.all()#issue_id,type_id,value的所有信息
    group_dict = get_project_map()#映射字典,给定一个id,返回其对应的项目群
    
    
    issue_dict = {}
    custom_value_dict = {}
    user_dict = {}
    for issue_info in issue_info_list:
        id=issue_info.id
        subject=issue_info.subject.encode("utf-8")
        issue_dict[id] = [issue_info.id,subject,issue_info.assigned_to_id,issue_info.project_id,issue_info.status_id]
    for customvalue in customvalues_list:
        customized_id=customvalue.customized_id
        custom_field_id=customvalue.custom_field_id
        value = ""
        if customvalue.value:
            value=customvalue.value.encode("utf-8")
        if customized_id not in custom_value_dict:
            custom_value_dict[customized_id] = {}
        custom_value_dict[customized_id][custom_field_id] = value
    for user in user_list:
        user_dict[user.id]=user.lastname+user.firstname
    for issue_id in issue_dict:
        raw_id,subject,assigned_to_id,project_id,status_id = issue_dict[issue_id]
        issue_one = [subject]#一共22列,这是第一列
        issue_1 =raw_id
        issue_2 = status_id
        username=user_dict.get(assigned_to_id)
        groupname = group_dict.get(project_id,"未知")
        for type in id_val_map:
            type_value = custom_value_dict[issue_id].get(type,"")
            issue_one.append(type_value)
        issue_one.append(username)
        issue_one.append(groupname)
        subject_info_tmp = CM_BaseLine_Subject_Info(raw_id =issue_1,status_id=issue_2,subject = issue_one[0],work_type = issue_one[1],start_time = issue_one[2],
                                                    due_time = issue_one[3],update_type = issue_one[4],version_num = issue_one[5],
                                                    old_version_num = issue_one[6],publish_version_num = issue_one[7],online_version_num = issue_one[8],
                                                    approve_person = issue_one[9],environment_fir = issue_one[10],environment_sec = issue_one[11],
                                                    environment_thi = issue_one[12],update_date = issue_one[13],change_content = issue_one[14],
                                                    update_method = issue_one[15],db_changed = issue_one[16],client_content = issue_one[17],
                                                    base_line_num = issue_one[18],update_book_num = issue_one[19],work_num = issue_one[20],problem_source = issue_one[21],
                                                    problem_type = issue_one[22], update_reason =issue_one[23], author_name = issue_one[24], project = issue_one[25])
        subject_info_tmp.save()#插入     
        '''error数据表插入'''   
        if(len(issue_one[22])>0):#若存在问题
            base_error_tmp = CmVrmsBaselineErrors(raw_id =issue_1,status_id=issue_2,subject = issue_one[0],UpdateDate = issue_one[2],
                                                    author_name = issue_one[24], project = issue_one[25],
                                                    problem_type = issue_one[22], problem_source = issue_one[21])
        try:
            base_error_tmp.save()
        except:
            pass             
        
        '''base_info数据表插入'''   
        environment_fir = issue_one[10]
        update_type = issue_one[4]
        if ("V" not in subject) and ("v" not in subject):
            continue
        if ('UAT' not in environment_fir) and ('模拟' not in environment_fir):
            continue#这些情况不需要考虑
        if ('升级' not in update_type) and ('版本同步' not in update_type) and ('模拟发布' not in update_type):
            continue

        
        
        app_name = subject.split("V")[0].split("v")[0].strip()
        app_name = app_name.strip("\\")
        NAME_MAP = NamemapInfo().namemap_info
        if len(app_name) < 2:
            continue
        if app_name in NAME_MAP:
            app_name = NAME_MAP[app_name]
        publish_version_num_str = issue_one[7]#此处需要对版本进行验证
        version_matchs = re.findall(r"[\.\d]+",publish_version_num_str)
        publish_version_num = ""
        if len(version_matchs)>0:
            nums = version_matchs[0].split(".")
            if len(nums) == 2:
                nums.append("0")
            if len(nums) == 3:
                nums.append("0")
            if len(nums) == 4:
                publish_version_num = "V{}.{}.{}.{}".format(*nums)
            if len(nums)>4:
                nums = nums[0:4]
                publish_version_num = "V{}.{}.{}.{}".format(*nums)
        if publish_version_num == "":#如果版本号这一关不符合规范
            continue
        update_date = issue_one[13]
        base_line_num = issue_one[18]
        update_book_num = issue_one[19]
        work_num = issue_one[20]
        """
        base_info_tmp = CM_BaseLine_Info(AppName = app_name,AppVersion = publish_version_num,
                                         UpdateDate=update_date,BaseLine = base_line_num,
                                        PageNumber = update_book_num,UppradeTime = work_num,
                                        version_num = issue_one[5],environment_fir = issue_one[10],
                                        UpgradeMan = issue_one[23], project = issue_one[24],
                                        problem_type = issue_one[22], problem_source = issue_one[21])
        """
        base_info_tmp = CM_BaseLine_Info(raw_id =issue_1,status_id=issue_2,AppName = app_name,AppVersion = publish_version_num,
                                         UpdateDate=update_date,BaseLine = base_line_num,
                                        PageNumber = update_book_num,UppradeTime = work_num,
                                        version_num = issue_one[5],environment_fir = issue_one[10],
                                        UpgradeMan = issue_one[24], project = issue_one[25],update_reason = issue_one[23],
                                        problem_type = issue_one[22], problem_source = issue_one[21],update_type = issue_one[4])
        
        try:
            base_info_tmp.save()
        except:
            pass
        
       
                        
        
    return HttpResponseRedirect('/cm_bi_index/')#重定向



def get_version_info_from_work_bi(request):
    '''由issue表和conf表和user表,更新require_issues表'''
    #id,project.name,i.subject,user.login,
    #{9:"紧迫程度",10:"提出部门",12:"需求提出原因",216:"期望上线时间",187:"需求类型*",14:"需求实现系统*",19:"计划上线版本",191:"项目组负责人*",127:"主系统名称*",193:"主版本号*"}
    CmVrmsBaselineRequire.objects.all().delete()#首先全部删除该表
    id_val_map = [9,10,12,216,187,14,19,191,127,193]
    #id_val_map = {9:"emergence",10:"proposed_department",12:"reason",216:"due_time",187:"require_type",14:"require_system",19:"version",191:"owner",127:"main_system_name",193:"main_ver_num"}
    issue_info_list = CmVrmsBaselineIssues.objects.all()#issue所有信息
    customvalues_list = CmVrmsBaselineCustomValues.objects.all()#issue_id,type_id,value的所有信息
    user_list = CmVrmsBaselineUsers.objects.all()#issue_id,type_id,value的所有信息
    project_list = CmVrmsBaselineProjects.objects.all()#project的信息,获取应用到每个项目群的映射关系
    
    
    issue_dict = {}
    custom_value_dict = {}
    user_dict = {}
    project_dict = {}
    for issue_info in issue_info_list:
        id=issue_info.id
        if id == 40779:
            print "succ"
        tracker_id = issue_info.tracker_id
        if tracker_id != 41:#只有tracker_id==41时才纳入考虑
            continue
        subject=issue_info.subject.encode("utf-8")
        issue_dict[id] = [issue_info.id,subject,issue_info.project_id,issue_info.author_id]
    for customvalue in customvalues_list:
        customized_id=customvalue.customized_id
        if customized_id not in issue_dict:
            continue#如果customized_id不在所需的issue范围内,则舍弃
        custom_field_id=customvalue.custom_field_id
        value = ""
        if customvalue.value:
            value=customvalue.value.encode("utf-8")
        if customized_id not in custom_value_dict:
            custom_value_dict[customized_id] = {}
        custom_value_dict[customized_id][custom_field_id] = value
    for user in user_list:
        user_dict[user.id]=user.lastname+user.firstname
    for project in project_list:
        project_dict[project.id] = project.name
        
    for issue_id in issue_dict:
        issue_id,subject,project_id,author_id = issue_dict[issue_id]
        project_name = project_dict[project_id]
        user_name = user_dict[author_id]
        
        issue_one = []#一共12列,这是第一列
        issue_one.append(issue_id)
        issue_one.append(project_name)
        issue_one.append(subject)
        issue_one.append(user_name)
        for type in id_val_map:
            
            type_value = custom_value_dict.get(issue_id,{}).get(type,"")
            issue_one.append(type_value)
        
        requir_info_tmp = CmVrmsBaselineRequire(issue_id =issue_one[0],project_name =issue_one[1],
                                                 subject =issue_one[2],user_name =issue_one[3],
                                                 emergence =issue_one[4],proposed_department =issue_one[5],
                                                 reason =issue_one[6],due_time =issue_one[7],
                                                 require_type =issue_one[8],require_system =issue_one[9],
                                                 version =issue_one[10],owner =issue_one[11],
                                                 main_system_name = issue_one[12],main_ver_num = issue_one[13]
                                                 )
        
        requir_info_tmp.save()#插入 
         
    insert_into_version(request)   
    
    return HttpResponseRedirect('/version_detail/')#重定向

def parse_subject_info(subject,version,main_system):
    #XXXX系统通过XXXX（IMIX、ETL、FTS中的一个）方式向XXXX系统获取XXXXXX数据
    try:
        sys_name_a = subject.split("通过")[0]
        depend_detail = subject.split("系统通过")[1].split("从")[0]
        depend_detail = "{} {}(同步)".format(depend_detail,version)#需要增加联测信息时,写成"{} {}(同步)、{} {}(联测)"的形式
        sys_name_b = subject.split("从")[1].split("获取")[0]
        data_interaction_detail = subject.split("系统获取")[1]
        data_flow = "->"
        if sys_name_a == main_system:
            data_flow = "<-"
            #如果sys_name_a就是主系统,则返回对应系统的信息
            return {sys_name_b:[data_flow,depend_detail,data_interaction_detail]}
        #如果sys_name_a不是主系统,则说明sys_name_b是主系统,返回对应系统的信息
        return {sys_name_a:[data_flow,depend_detail,data_interaction_detail]}
    except:
        return {}
def convert_version(publish_version_num_str):
    version_matchs = re.findall(r"[\.\d]+",publish_version_num_str)
    publish_version_num = ""
    if len(version_matchs)>0:
        nums = version_matchs[0].split(".")
        if len(nums) == 2:
            nums.append("0")
        if len(nums) == 3:
            nums.append("0")
        if len(nums) == 4:
            publish_version_num = "V{}.{}.{}.{}".format(*nums)
        if len(nums)>4:
            nums = nums[0:4]
            publish_version_num = "V{}.{}.{}.{}".format(*nums)
    return publish_version_num

def insert_into_version(request):
    
    VerConfInfo.objects.filter(remark_col1='').delete()#将未修改的行全部删除
    '''无需考虑进关系的requir_system'''
    un_need_requir_system = set(['实时消息传输中间件','文件传输中间件','数据传输中间件','IMIX','ETL','IMIX协议'])
    map_node_conf = {"实时消息传输中间件":"IMIX",
                     "数据传输中间件":"ETL",
                     "文件传输中间件":"FTP",
                     "IMIX":"IMIX",
                     "ETL":"ETL",
                     "IMIX协议":"IMIX",
                     }

    '''获取system info里面的信息， 同步到version中来'''
    system_info = SystemInfo().sys_info
    '''从数据库中，将待version化数据读取出来'''
    requir_issue_info_list = CmVrmsBaselineRequire.objects.all()#所有需要的issue所有信息
    project_info = {}
    project_main_system = {}
    for issue in requir_issue_info_list:
        project_name = issue.project_name.encode("utf-8")
        if "BPM" in project_name:
            continue
        
        require_system =issue.require_system.encode("utf-8")
        require_system = convert_name(require_system)
        if len(require_system.strip()) == 0:
            continue
        subject = issue.subject.encode("utf-8")
        version =issue.version.encode("utf-8")
        version = convert_version(version)
        if len(version) == 0:
            continue
        main_system_name = issue.main_system_name.encode("utf-8")
        if len(main_system_name) != 0:
            project_main_system[project_name] = main_system_name
        if project_name not in project_info:
            project_info[project_name] = []
        tmp_need_info = [subject,require_system,version]
        project_info[project_name].append(tmp_need_info)
    for project_name in project_info:
        '''获取主系统名称'''
        main_system = project_main_system.get(project_name,"")
        info_list = project_info[project_name]
        if len(main_system) == 0:
            require_system_list = [val[1] for val in info_list if val[1] not in un_need_requir_system]
            require_system_set = set(require_system_list)
            system_count = 0 
            for require_name in require_system_set:
                tmp_count = require_system_list.count(require_name)
                if tmp_count > system_count:
                    main_system = require_name#若新出现的require system的次数较多，则更新主系统名字
                    system_count = tmp_count
        '''拼接后续的其他系统'''
        #主系统对应的所有版本号
        main_version_list = set([val[2] for val in info_list if val[1]==main_system and len(val[2])>0])
        if len(main_version_list) == 0:
            continue
        #从readmine里面获取的，该主系统对应的所有其他系统及其版本
        subject_list = [[val[0],val[2]] for val in info_list if val[1] in un_need_requir_system]#存放subject及对应的version
        subject_info_data = {}#记录的是  对应的sys name->[data_flow,depend_detail,data_interaction_detail]
        for subject_info in subject_list:
            subject,version = subject_info
            subject_info_data.update(parse_subject_info(subject,version,main_system))
        have_cover_version = set([subject_info_data[val][1].split("(")[0] for val in subject_info_data])#列举出已经出现了的ETL VXXXX这样的信息
        all_need_middle_ware_node = set(["{} {}".format(map_node_conf[val[1]],val[2]) for val in info_list if val[1] in un_need_requir_system])#枚举出所有中间件的信息
        all_need_middle_ware_node = [val for val in all_need_middle_ware_node if val not in have_cover_version]#从中排除掉已经出现了的信息
        all_need_middle_ware_node = [val.split(" ") for val in all_need_middle_ware_node]
        all_need_middle_ware_node = [[val[0],val[1],"Y","Y"] for val in all_need_middle_ware_node]
        #传输中间件系统也同时置为同步状态
        middle_subject_info_data = {}
        for val in all_need_middle_ware_node:
            middle_subject_info_data[val[0]+val[1]] = ["->","{} {}(同步)".format(val[0],val[1]),""]
        
            
                    
        other_nodes_from_info = [[val[1],val[2],"Y","Y"] for val in info_list if val[1] not in un_need_requir_system and val[1]!=main_system]
        other_nodes_from_info_set = set([val[0] for val in other_nodes_from_info])
        other_nodes_from_subjectinfo = [[val,"","N","N"] for val in subject_info_data if val not in un_need_requir_system and val!=main_system and val not in other_nodes_from_info_set]
        other_nodes_from_subjectinfo_set = set([val[0] for val in other_nodes_from_subjectinfo])
        other_nodes_from_sys = [[val,"","N","N"] for val in system_info.get(main_system,[]) if ((val not in other_nodes_from_subjectinfo_set) and (val not in other_nodes_from_info_set))]#来自于system的其余node,要排除掉在group中已经出现的节点,以及从subject中抽取得到的节点
        other_nodes = other_nodes_from_info+ other_nodes_from_subjectinfo + other_nodes_from_sys + all_need_middle_ware_node

        for main_version in  main_version_list:
            main_up_sys_name = main_system
            main_up_sys_version = main_version
            if len(main_up_sys_name) == 0 or len(main_up_sys_version) == 0:
                continue
            for targe_info in other_nodes:
                relevant_sys_name,relevant_sys_version,main_relevant_con_if_test,main_relevant_con_if_sync = targe_info
                #同一关联系统版本号可能有多个且有误，此处先不生成关联系统的版本号，暂时设为空值，后续有需要可以去掉
                relevant_sys_version = ""
                if len(relevant_sys_name) == 0:
                    continue
                main_up_sys_data_flow,depend_detail,data_interaction_detail = subject_info_data.get(relevant_sys_name,["","",""])
                #当中间件系统没有作为传输介质时，则作为目标系统
                if relevant_sys_name+relevant_sys_version in middle_subject_info_data:
                    main_up_sys_data_flow,depend_detail,data_interaction_detail = middle_subject_info_data[relevant_sys_name+relevant_sys_version]
                
                try:#如果已经存在,则不修改
                    conf_info_tmp = VerConfInfo.objects.get(main_up_sys_name=main_up_sys_name,
                                        main_up_sys_version=main_up_sys_version,
                                        relevant_sys_name=relevant_sys_name,
                                        relevant_sys_version=relevant_sys_version)
                except VerConfInfo.DoesNotExist:
                    try:
                        if "央行" in main_up_sys_name or "央行" in relevant_sys_name:
                            continue
                           
                        conf_info_tmp = VerConfInfo(main_up_sys_name=main_up_sys_name, 
                                      main_up_sys_version=main_up_sys_version,
                                      main_up_sys_data_flow=main_up_sys_data_flow,
                                      relevant_sys_name=relevant_sys_name,
                                      relevant_sys_version=relevant_sys_version,
                                      main_relevant_con_if_test=main_relevant_con_if_test,
                                      main_relevant_con_if_sync=main_relevant_con_if_sync,
                                      depend_detail=depend_detail,
                                      data_interaction_detail=data_interaction_detail
                                      )
                        conf_info_tmp.save()#插入  
                    except:
                        print "error"     
    return HttpResponseRedirect('/version_detail/')#重定向

                    
        
def get_updatetime_from_db(request):
    UpdatetimeInfo.objects.all().delete()
    cursor1 = connection.cursor() 
    cursor1.execute("INSERT INTO  update_time (AppName,AppVersion,UpdateDate,environment_fir) select AppName,AppVersion,min(UpdateDate),environment_fir from cm_vrms_baseline_cm_baseline_info GROUP BY AppName,AppVersion")
    return HttpResponseRedirect('/version_detail/')#重定向
    
        
 
