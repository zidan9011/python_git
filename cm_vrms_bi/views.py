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
from django.db.models import Avg, Max, Min, Count
from django.shortcuts import render_to_response
import MySQLdb
import datetime
import re
import time
from django.db import connection,transaction
from .models import CqUatst
def get_last_day(dtstr):
    #输入形如 "02 2015"格式的字符串,返回对应四个日期的字符串
    try:
        d_tm_first = datetime.datetime.strptime(dtstr,"%m %Y").date()
        d_next = d_tm_first + datetime.timedelta(days=31)
        d_tm_last = datetime.datetime.strptime(d_next.strftime("%Y %m"),"%Y %m").date() - datetime.timedelta(days=1)
        d_lm_last = d_tm_first - datetime.timedelta(days=1)
        d_lm_first = datetime.datetime.strptime(d_lm_last.strftime("%Y %m"),"%Y %m").date()
        this_month_last = d_tm_last.strftime("%Y-%m-%d")
        this_month_first = d_tm_first.strftime("%Y-%m-%d")
        last_month_last = d_lm_last.strftime("%Y-%m-%d")
        last_month_first = d_lm_first.strftime("%Y-%m-%d")    
        return [this_month_first,this_month_last,last_month_first,last_month_last]
    except:
        return None

def get_index_info(appname,appversion,last_month_first,this_month_last):
    cursor = connection.cursor()
    need_sql = "SELECT AppName,AppVersion,UpdateDate,BaseLine,PageNumber,UppradeTime,version_num,environment_fir,UpgradeMan,update_reason,project FROM cm_vrms_baseline_cm_baseline_info where update_type = '升级' and environment_fir !='模拟环境' and  AppName = '"+appname+"' and AppVersion like '%"+appversion+"%' and UpdateDate <= '"+this_month_last+"' order by UpdateDate desc;" 
    cursor.execute(need_sql)
    count_currentnum = cursor.fetchall()
    out_str = ""
    for val in count_currentnum:
        AppName,AppVersion,UpdateDate,BaseLine,PageNumber,UppradeTime,version_num,environment_fir,UpgradeMan,update_reason,project = val
        format_str =  "<tr>"+"<td>{}</td>"*len(val)+"</tr>"
        out_str += format_str.format(*val)
    #该项目版本历次升级信息的详情展示
    out_str = out_str.encode("utf-8")
    return out_str 

def cm_bi_index(request):
    c = Context({'STATIC_URL': '/static/'})
    out_path = "cm_bi_index"  
    str_need_date_time_start = ""
    str_need_date_time = ""
    day_list = None
    try:
        str_need_date_time_start = request.GET["query1"].encode("utf-8")#获取搜索框中的时间
        str_need_date_time_end = request.GET["query2"].encode("utf-8")#获取搜索框中的时间
        day_list = get_last_day(str_need_date_time)
    except:
        str_need_date_time = datetime.datetime.now().strftime("%m %Y")#若没有query,则默认为今天
        day_list = get_last_day(str_need_date_time)#this_month_first,this_month_last,last_month_first,last_month_last
        day_list[1] = datetime.datetime.now().strftime("%Y-%m-%d")
    if not day_list:#如果输入的日期还是有错误
        str_need_date_time = datetime.datetime.now().strftime("%m %Y")#若没有query,则默认为今天
        day_list = get_last_day(str_need_date_time)
        day_list[1] = datetime.datetime.now().strftime("%Y-%m-%d")

    
    this_month_first,this_month_last,last_month_first,last_month_last = day_list
    if len(str_need_date_time_start) > 0 and len(str_need_date_time_end):#如果有用户查找,则按照他们选择的日期进行查找
        this_month_first = str_need_date_time_start
        this_month_last = str_need_date_time_end
    cursor1 = connection.cursor() 
    cursor1.execute("SELECT COUNT(AppName) FROM `cm_vrms_baseline_cm_baseline_info` where status_id !=5 and environment_fir !='模拟环境' and update_type !='模拟发布' and UpdateDate BETWEEN '"+this_month_first+"' and '"+this_month_last+"';")
    count_total = cursor1.fetchall()
    cursor2 = connection.cursor()
    cursor2.execute("SELECT COUNT(id) FROM `cm_vrms_baseline_errors` where status_id !=5 and UpdateDate BETWEEN '"+this_month_first+"' and '"+this_month_last+"' and problem_type LIKE 'A%';")
    count_Pro_A = cursor2.fetchall()
    cursor3 = connection.cursor()
    cursor3.execute("SELECT COUNT(id) FROM `cm_vrms_baseline_errors` where status_id !=5 and UpdateDate BETWEEN '"+this_month_first+"' and '"+this_month_last+"' and problem_type LIKE 'B%';")
    count_Pro_B = cursor3.fetchall()
    cursor5 = connection.cursor()
    cursor5.execute("SELECT COUNT(CaSystemName) FROM `cq_uatst` where submitdate BETWEEN '"+this_month_first+" 00:00:00' and '"+this_month_last+" 23:59:59' ;")
    count_envi_Pro = cursor5.fetchall()
    c['count_total_result'] = count_total[0][0]
    c['count_A_pro'] = count_Pro_A[0][0]
    c['count_B_pro'] = count_Pro_B[0][0]
    c['count_envi_Pro'] = count_envi_Pro[0][0]
    cursor4 = connection.cursor()
    cursor4.execute("select AppName,AppVersion,version_num FROM `cm_vrms_baseline_cm_baseline_info` where UpdateDate between '"+this_month_first+"' and '"+this_month_last+"' and version_num >=4 ORDER BY UpdateDate;")
    count_sys = cursor4.fetchall()

    sys_up_count_dict = {}
    for count_info in count_sys:
        appname,appversion,version_num = count_info
        version_num = int(version_num)
        if ("本币交易系统" not in appname.encode("utf8")) and ("本币结算代理模块" not in appname.encode("utf8")) and ("本币利率互换模块" not in appname.encode("utf8")) and ("本币外部交易确认模块" not in appname.encode("utf8")):
            appversion = ".".join(appversion.split(".")[:-1])#移除最后一位
        key = appname+" "+appversion
        sys_up_count_dict[key] = version_num
    sys_up_count_list = sorted(sys_up_count_dict.items(),key = lambda k:k[1])
    sys_name_list = [val[0] for val in sys_up_count_list]
    sys_count_list = [val[1] for val in sys_up_count_list]
    
    #系统升级信息详情
    sys_update_info = ""
    for name_version in sys_name_list:
        appname,appversion = name_version.split(" ")
        detail_table = get_index_info(appname,appversion,this_month_first,this_month_last)
        table_format = '<table class=\'table table-condensed\'><caption>{}的升级详情</caption><thead><tr><th>应用系统名称</th><th>应用系统版本号</th><th>升级时间</th><th>代码基线号</th><th>升级步骤页数</th><th>工作量</th><th>补丁号</th><th>升级环境（一级）</th><th>指派给</th><th>升级原因</th><th>项目群</th></tr></thead><tbody>{}</tbody></table>'.format(name_version,detail_table)
        sys_update_info += '"{}":"{}",'.format(name_version,table_format)
    c["sys_update_info"] = "{"+ sys_update_info + "}"
    
    len_num0 = 30*len(sys_name_list)
    len_num = max(300,len_num0)
    color_list = []
    for count in sys_count_list:
        color = ""
        if count > 7:
            color = "#C1232B"
        elif count > 6:
            color = "#F0805A"
        elif count > 5:
            color = "#F0805A"
        elif count > 4:
            color = "#F0805A"       
        else:
            color = "#FAD860"
        color_list.append(color)
    c['sys_name_list'] = sys_name_list
    c['sys_count_list'] = sys_count_list    
    c['color_count_list'] = color_list    

    
    c['month_tag'] = datetime.datetime.strptime(this_month_first,"%Y-%m-%d").date().strftime("%Y年%m月 %d日")+" 至 "+datetime.datetime.strptime(this_month_last,"%Y-%m-%d").date().strftime("%Y年%m月 %d日")
    c['month_jump'] = datetime.datetime.strptime(this_month_last,"%Y-%m-%d").date().strftime("%m-%Y")
    c['len_num']=len_num
    return render_to_response(out_path+'.html',context_instance=c)

def bi_update(request):
    c = Context({'STATIC_URL': '/static/'})
    out_path = "bi_update"
    str_need_date_time = ""
    try:#如果由用户选择
        str_need_date_time = request.GET["query"].encode("utf-8")#获取搜索框中的时间
    except:
        str_need_date_time = request.path[:-1].replace("/bi_update","").encode("utf-8")
        str_need_date_time = str_need_date_time.replace("-"," ")
    if len(str_need_date_time) < 1:
        str_need_date_time = datetime.datetime.now().strftime("%m %Y")#若没有query,则默认为今天
    day_list = get_last_day(str_need_date_time)#this_month_first,this_month_last,last_month_first,last_month_last
    if not day_list:#如果输入的日期还是有错误
        str_need_date_time = datetime.datetime.now().strftime("%m %Y")#若没有query,则默认为今天
        day_list = get_last_day(str_need_date_time)
    
    this_month_first,this_month_last,last_month_first,last_month_last = day_list
        
    cursor1 = connection.cursor() 
    cursor1.execute("select project,COUNT(AppName) from cm_vrms_baseline_cm_baseline_info where status_id !=5 and environment_fir !='模拟环境' and update_type !='模拟发布' and UpdateDate BETWEEN '"+this_month_first+"' and '"+this_month_last+"' GROUP  BY project;")
    count_currentnum = cursor1.fetchall()
    current_num = dict([[val[0],int(val[1])] for val in count_currentnum])
    
    cursor2 = connection.cursor() 
    cursor2.execute("SELECT project,COUNT(AppName) FROM cm_vrms_baseline_cm_baseline_info where status_id !=5 and environment_fir !='模拟环境' and update_type !='模拟发布' and UpdateDate BETWEEN  '"+last_month_first+"' and '"+last_month_last+"' GROUP  BY project;")
    count_lastmonthnum = cursor2.fetchall()
    last_num = dict([[val[0],int(val[1])] for val in count_lastmonthnum])
    
    all_projects_list = sorted(list(set(current_num.keys() + last_num.keys())))
    all_projects_list = [val for val in all_projects_list if "未知" not in val]
    all_projects_current = []
    all_projects_last = []
    for project in all_projects_list:
        all_projects_current.append(current_num.get(project,0))
        all_projects_last.append(last_num.get(project,0))
    #当天
    now = datetime.datetime.strptime(this_month_first,"%Y-%m-%d").date()
    #上月1号
    last = datetime.datetime.strptime(last_month_first,"%Y-%m-%d").date()
    
    now_month = "{}月".format(now.strftime('%m'))
    last_month = "{}月".format(last.strftime('%m'))        
    c['last_month'] = last_month
    c['current_month'] = now_month
    c['all_projects_list'] = all_projects_list
    #取该群真正的名字
    c['all_projects_list'] = [c['all_projects_list'][i].split()[-1] for i in range(len(c['all_projects_list']))]#增加\n
    c['all_projects_current'] = all_projects_current
    c['all_projects_last'] = all_projects_last          

    out_str = ""  
    for i,name in enumerate(all_projects_list):
        name = name.split()[-1]
        down_ratio = "/"
        if all_projects_last[i] > 0:
            down_ratio = (all_projects_current[i] - all_projects_last[i])/(all_projects_last[i] + 0.0)
            down_ratio = "{0:.4}%".format(down_ratio*100)
        out_str += "<tr><td>{}</td><td>{}</td></tr>".format(name,down_ratio)
    c["out_str"] = out_str      
    
    c['month_tag'] = datetime.datetime.strptime(this_month_first,"%Y-%m-%d").date().strftime("%Y年%m月 ")
    c['month_jump'] = datetime.datetime.strptime(this_month_first,"%Y-%m-%d").date().strftime("%m-%Y")
    
    return render_to_response(out_path+'.html',context_instance=c)


def get_problem_num(count_currentnum):
    current_info = {}
    for val in count_currentnum:
        if val[0] is not None:
            name = val[0].split()[-1]
        else:
            continue
        type = val[1].split("-")[0]
        count = int(val[2])
        if name not in current_info:
            current_info[name] = {}
        current_info[name][type] = count
        
    current_info_join = {}
    for name in current_info:
        a_type = current_info[name].get("A",0)
        b_type = current_info[name].get("B",0)
        c_type = current_info[name].get("C",0)
        d_type = current_info[name].get("D",0)
        current_info_join[name]= {}
        current_info_join[name]["AB"] = a_type+b_type
        current_info_join[name]["CD"] = c_type+d_type   
    return current_info_join 

def get_problem_info(project_name,last_month_first,this_month_last):
    cursor = connection.cursor() 
    cursor.execute("SELECT project,raw_id,subject,UpdateDate,problem_source,problem_type,author_name FROM cm_vrms_baseline_errors where status_id !=5 and project like '%"+project_name+"%' and UpdateDate BETWEEN '"+last_month_first+"' and '"+this_month_last+"' order by UpdateDate desc;")
    count_currentnum = cursor.fetchall()
    out_str = ""
    for val in count_currentnum:
        project,raw_id,subject,UpdateDate,problem_source,problem_type,author_name = val
        project = project.split()[-1]
        problem_type = problem_type.split("-")[0]
        out_str += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(project,raw_id,subject,UpdateDate,problem_source,problem_type,author_name)
    #改项目群下所有错误的详细信息
    out_str = out_str.encode("utf-8")
    return out_str 


def bi_problem(request):
    need_list = [u'本币项目群',u'外汇项目群',u'数据平台项目群',u'信息项目群',u'交易后项目群',u'央行项目群',u'基础设施项目群',u'SWAP项目群',u'互联网项目群']
    c = Context({'STATIC_URL': '/static/'})
    out_path = "bi_problem"  
    str_need_date_time = ""
    try:#如果有用户选择
        str_need_date_time = request.GET["query"].encode("utf-8")#获取搜索框中的时间
    except:
        str_need_date_time = request.path[:-1].replace("/bi_problem","").encode("utf-8")
        str_need_date_time = str_need_date_time.replace("-"," ")
    if len(str_need_date_time) < 1:
        str_need_date_time = datetime.datetime.now().strftime("%m %Y")#若没有query,则默认为今天
    day_list = get_last_day(str_need_date_time)#this_month_first,this_month_last,last_month_first,last_month_last
    if not day_list:#如果输入的日期还是有错误
        str_need_date_time = datetime.datetime.now().strftime("%m %Y")#若没有query,则默认为今天
        day_list = get_last_day(str_need_date_time)
    
    this_month_first,this_month_last,last_month_first,last_month_last = day_list

    
    cursor1 = connection.cursor() 
    cursor1.execute("SELECT project,problem_type,COUNT(id) FROM cm_vrms_baseline_errors where status_id !=5 and  UpdateDate BETWEEN '"+this_month_first+"' and '"+this_month_last+"' GROUP  BY project,problem_type;")
    count_currentnum = cursor1.fetchall()
    current_info_join = get_problem_num(count_currentnum)

    cursor2 = connection.cursor() 
    cursor2.execute("SELECT project,problem_type,COUNT(id) FROM cm_vrms_baseline_errors where status_id !=5 and  UpdateDate BETWEEN '"+last_month_first+"' and '"+last_month_last+"' GROUP  BY project,problem_type;")
    count_lastnum = cursor2.fetchall()
    last_info_join = get_problem_num(count_lastnum)
    
    last_num_ab = []
    last_num_cd = []
    curr_num_ab = []
    curr_num_cd = []
    for sys_name in need_list:
        l_ab = last_info_join.get(sys_name,{}).get("AB",0)
        l_cd = last_info_join.get(sys_name,{}).get("CD",0)
        c_ab = current_info_join.get(sys_name,{}).get("AB",0)
        c_cd = current_info_join.get(sys_name,{}).get("CD",0)
        last_num_ab.append(l_ab)
        last_num_cd.append(l_cd)
        curr_num_ab.append(c_ab)
        curr_num_cd.append(c_cd)
    #当天
    now = datetime.datetime.strptime(this_month_first,"%Y-%m-%d").date()
    #上月1号
    last = datetime.datetime.strptime(last_month_first,"%Y-%m-%d").date()
    
    now_month = "{}月".format(now.strftime('%m'))
    last_month = "{}月".format(last.strftime('%m'))

    month_list = [last_month,now_month]*len(need_list)
    
    c["now_month"] = now_month
    c["last_month"] = last_month
    c["month_list"] = month_list
    c["need_list"] = need_list
    c["last_num_ab"] = last_num_ab
    c["last_num_cd"] = last_num_cd
    c["curr_num_ab"] = curr_num_ab
    c["curr_num_cd"] = curr_num_cd  
    
    out_str = ""  
    for i,name in enumerate(need_list):
        ab_down_ratio = "/"
        cd_down_ratio = "/"
        if last_num_ab[i] > 0:
            ab_down_ratio = (curr_num_ab[i] - last_num_ab[i])/(last_num_ab[i] + 0.0)
            ab_down_ratio = "{0:.4}%".format(ab_down_ratio*100)
        if last_num_cd[i] > 0:
            cd_down_ratio = (curr_num_cd[i] - last_num_cd[i])/(last_num_cd[i] + 0.0)
            cd_down_ratio = "{0:.4}%".format(cd_down_ratio*100)
        out_str += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(name,ab_down_ratio,cd_down_ratio)
    
    #项目群错误信息详情
    project_error_info = ""
    for project_name in need_list:
        detail_table = get_problem_info(project_name,last_month_first,this_month_last)
        table_format = '<table class=\'table\'><caption>{}的错误详情</caption><thead><tr><th>项目群名称</th><th>任务号</th><th>具体错误内容</th><th>开始时间</th><th>问题原因</th><th>问题类型</th><th>指派给</th></tr></thead><tbody>{}</tbody></table>'.format(project_name,detail_table)
        project_error_info += '"{}":"{}",'.format(project_name,table_format)

            
    c["out_str"] = out_str  
    c["project_error_info"] = "{"+ project_error_info + "}"
    
    
    c['month_tag'] = datetime.datetime.strptime(this_month_first,"%Y-%m-%d").date().strftime("%Y年%m月 ")
    c['month_jump'] = datetime.datetime.strptime(this_month_first,"%Y-%m-%d").date().strftime("%m-%Y")
    
    return render_to_response(out_path+'.html',context_instance=c)

def get_envi_prob_info(casystemname,this_month_first,this_month_last):
    cursor = connection.cursor()
    need_sql = "select id,subsystemname,versionNo,testenv,casystemname,submitdate,bugtype_1,bugtype_2,bugtype_3,severity,rate,impactnum,impatstart,impatend,state,headline,description,defecttype,resolution,ITIL_ID,submitter,principal,owner_old,analysisresult,check_date,assign_date,open_date,planstart,planfinish,actualstart,actualfinish,Resolve_date,validate_date,close_date,prjno,prjname  FROM `cq_uatst` where casystemname = '"+casystemname+"' and submitdate between '"+this_month_first+" 00:00:00' and '"+this_month_last+" 23:59:59' ORDER BY submitdate;" 
    cursor.execute(need_sql)
    count_currentnum = cursor.fetchall()
    out_str = ""
    for val in count_currentnum:
        
        format_str =  "<tr>"+"<td>{}</td>"*len(val)+"</tr>"
        out_str += format_str.format(*val)
    #该项目群下所有环境问题的详细信息
    out_str = out_str.encode("utf-8")
    out_str = out_str.replace("+00:00","")
    return out_str 

def get_envi_problem_num(count_currentnum):
    current_info = {}
    for val in count_currentnum:
        if val[0].strip() =='':
            continue
        type = val[0].split("-")[1]
        count = int(val[1])
        current_info[type] = count
    current_info_join = []
    current_info_join.append(current_info.get(u"技术原因",0))
    current_info_join.append(current_info.get(u"数据原因",0))
    current_info_join.append(current_info.get(u"操作原因",0))

    return current_info_join 

def get_envi_down_ration(this_month_first,this_month_last,last_month_first,last_month_last):
    cursor1 = connection.cursor() 
    cursor1.execute("SELECT bugtype_1,COUNT(id) FROM cq_uatst where submitdate BETWEEN '"+this_month_first+" 00:00:00' and '"+this_month_last+" 23:59:59'  group by bugtype_1 order by bugtype_1;")
    count_currentnum = cursor1.fetchall()
    current_info_join = get_envi_problem_num(count_currentnum)#int list,三种错误类型的排序

    cursor2 = connection.cursor() 
    cursor2.execute("SELECT bugtype_1,COUNT(id) FROM cq_uatst where submitdate BETWEEN '"+last_month_first+" 00:00:00' and '"+last_month_last+" 23:59:59'  group by bugtype_1 order by bugtype_1;")
    
    count_lastnum = cursor2.fetchall()
    last_info_join = get_envi_problem_num(count_lastnum)
    out_str = ""  
    header_list = ["技术原因","数据原因","操作原因"]
    for i,name in enumerate(current_info_join):
        down_ratio = "/"
        down_type = ""
        if last_info_join[i] > 0:
            down_type = header_list[i]
            down_ratio = (current_info_join[i] - last_info_join[i])/(last_info_join[i] + 0.0)
            down_ratio = "{0:.4}%".format(down_ratio*100)
        out_str += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(header_list[i],last_info_join[i],current_info_join[i],down_ratio) 
    return out_str


def bi_envi_prob(request):
    c = Context({'STATIC_URL': '/static/'})
    out_path = "bi_envi_prob"  
    str_need_date_time = ""
    try:#如果有用户选择
        str_need_date_time = request.GET["query"].encode("utf-8")#获取搜索框中的时间
    except:
        str_need_date_time = request.path[:-1].replace("/bi_envi_prob","").encode("utf-8")
        str_need_date_time = str_need_date_time.replace("-"," ")
    if len(str_need_date_time) < 1:
        str_need_date_time = datetime.datetime.now().strftime("%m %Y")#若没有query,则默认为今天
    day_list = get_last_day(str_need_date_time)#this_month_first,this_month_last,last_month_first,last_month_last
    if not day_list:#如果输入的日期还是有错误
        str_need_date_time = datetime.datetime.now().strftime("%m %Y")#若没有query,则默认为今天
        day_list = get_last_day(str_need_date_time)
    
    this_month_first,this_month_last,last_month_first,last_month_last = day_list

    #当月问题统计
    cursor1 = connection.cursor() 
    cursor1.execute("SELECT CaSystemName,COUNT(CaSystemName) num FROM `cq_uatst` where submitdate BETWEEN '"+this_month_first+" 00:00:00' and '"+this_month_last+" 23:59:59' group by CaSystemName order by num DESC;")
    count_currentnum = cursor1.fetchall()
    systemname_count_this = [[val[0],int(val[1])] for val in count_currentnum]#按照由大到小排序
    #上月问题统计
    cursor2 = connection.cursor() 
    cursor2.execute("SELECT CaSystemName,COUNT(CaSystemName) num FROM `cq_uatst` where submitdate BETWEEN '"+last_month_first+" 00:00:00' and '"+last_month_last+" 23:59:59' group by CaSystemName order by num DESC;")
    count_lastnum = cursor2.fetchall()
    systemname_count_last = dict([[val[0],int(val[1])] for val in count_lastnum])#方便本月信息在其内查找    
    down_rate_out_str = ""  
    #生成月环比下降信息
    for name,this_count in systemname_count_this:
        last_count = systemname_count_last.get(name,0)#上月问题次数
        down_ratio = "/"
        
        if last_count > 0:
            down_ratio = (this_count - last_count)/(last_count + 0.0)
            down_ratio = "{0:.4}%".format(down_ratio*100)
        down_rate_out_str += "<tr><td>{}</td><td>{}</td></tr>".format(name,down_ratio)
        
    #环境问题信息详情
    sys_name_list = [val[0] for val in systemname_count_this]#当月所有问题
    need_out_info_list = ["ID","系统名称","测试版本号","环境","引起问题的系统","提交时间","问题分类1","问题分类2","问题分类3","严重程度","优先级","影响人数","影响开始时间","影响完成时间","状态","问题标题","问题描述","问题原因","解决方案","ITIL单号","提交人","问题经理","问题分析人姓名","分析结论","核对时间","分派时间","打开时间","计划开始时间","计划完成时间","实际开始时间","实际完成时间","解决时间","验证时间","关闭时间","项目编号","项目名称"]
    need_out_info_str = "".join(["<th>{}</th>".format(val) for val in need_out_info_list])
    sys_problem_info = ""
    for casystemname in sys_name_list:
        detail_table = get_envi_prob_info(casystemname,this_month_first,this_month_last)
        table_format = '<table class=\'table\'><caption>{}的环境问题详情</caption><thead><tr>{}</tr></thead><tbody>{}</tbody></table>'.format(casystemname,need_out_info_str,detail_table)
        sys_problem_info += '"{}":"{}",'.format(casystemname,table_format)
    c["sys_problem_info"] = "{"+ sys_problem_info + "}"
    
    c['down_rate_out_str'] = down_rate_out_str#环比下降信息
    systemname_count_this_str = ",".join(["lkuohaovalue:{},name:'{}'rkuohao".format(val[1],val[0]) for val in systemname_count_this])
    systemname_count_this_str = systemname_count_this_str.replace("lkuohao", "{").replace("rkuohao", "}")
    c['systemname_count_this_str'] = systemname_count_this_str    

    c['sys_name_list'] = sys_name_list
    type_down_rate_out_str = get_envi_down_ration(this_month_first,this_month_last,last_month_first,last_month_last)
    c['type_down_rate_out_str'] = type_down_rate_out_str
    #当天
    now = datetime.datetime.strptime(this_month_first,"%Y-%m-%d").date()
    #上月1号
    last = datetime.datetime.strptime(last_month_first,"%Y-%m-%d").date()
    now_month = "{}月".format(now.strftime('%m'))
    last_month = "{}月".format(last.strftime('%m'))
    c["now_month"] = now_month
    c["last_month"] = last_month
    c['month_tag'] = datetime.datetime.strptime(this_month_first,"%Y-%m-%d").date().strftime("%Y年%m月 %d日")+" 至 "+datetime.datetime.strptime(this_month_last,"%Y-%m-%d").date().strftime("%Y年%m月 %d日")
    c['month_jump'] = datetime.datetime.strptime(this_month_last,"%Y-%m-%d").date().strftime("%m-%Y")
    return render_to_response(out_path+'.html',context_instance=c)

def bi_human(request):
    c = Context({'STATIC_URL': '/static/'})
    out_path = "bi_human"  
    str_need_date_time_start = ""
    str_need_date_time = ""
    day_list = None
    try:#如果由用户选择
        str_need_date_time_start = request.GET["query1"].encode("utf-8")#获取搜索框中的时间
        str_need_date_time_end = request.GET["query2"].encode("utf-8")#获取搜索框中的时间
        day_list = get_last_day(str_need_date_time)
    except:
        str_need_date_time = datetime.datetime.now().strftime("%m %Y")#若没有query,则默认为今天
        day_list = get_last_day(str_need_date_time)#this_month_first,this_month_last,last_month_first,last_month_last
        day_list[1] = datetime.datetime.now().strftime("%Y-%m-%d")
    if not day_list:#如果输入的日期还是有错误
        str_need_date_time = datetime.datetime.now().strftime("%m %Y")#若没有query,则默认为今天
        day_list = get_last_day(str_need_date_time)
        day_list[1] = datetime.datetime.now().strftime("%Y-%m-%d")
    
    
    this_month_first,this_month_last,last_month_first,last_month_last = day_list
    if len(str_need_date_time_start) > 0 and len(str_need_date_time_end):#如果有用户查找,则按照他们选择的日期进行查找
        this_month_first = str_need_date_time_start
        this_month_last = str_need_date_time_end
        
    cursor1 = connection.cursor() 
    cursor1.execute("select author_name, COUNT(id) from cm_vrms_baseline_cm_baseline_subject_info where (status_id !=5 and update_date between '"+this_month_first+"' and '"+this_month_last+"') and (environment_fir like '%UAT%' or environment_fir like'%模拟环境%') GROUP BY author_name;")
    count_currentnum = cursor1.fetchall()
    human_update_count_dict = {}
    for count_info in count_currentnum:
        author_name,update_num = count_info
        update_num = int(update_num)
        key = author_name
        human_update_count_dict[key] = update_num
    human_update_count_dict = sorted(human_update_count_dict.items(),key = lambda k:k[1],reverse=True)
    author_name_list = [val[0] for val in human_update_count_dict]
    update_num_list = [val[1] for val in human_update_count_dict]
    
    cursor2 = connection.cursor() 
    cursor2.execute("SELECT Principal, COUNT(Principal) FROM `cq_uatst` where submitdate BETWEEN '"+this_month_first+" 00:00:00' and '"+this_month_last+" 23:59:59' GROUP BY Principal;")
    count_vir_pro_num = cursor2.fetchall()
    human_vir_pro_count_dict = {}
    for count_vir_info in count_vir_pro_num:
        Principal,vir_pro_num = count_vir_info
        vir_pro_num = int(vir_pro_num)
        key = Principal
        human_vir_pro_count_dict[key] = vir_pro_num
    human_vir_pro_count_dict = sorted(human_vir_pro_count_dict.items(),key = lambda k:k[1],reverse=True)
    Principal_list = [val[0] for val in human_vir_pro_count_dict]
    vir_pro_num_list = [val[1] for val in human_vir_pro_count_dict]
    
    
    cursor3 = connection.cursor() 
    cursor3.execute("select author_name, problem_type, COUNT(problem_type) from cm_vrms_baseline_errors where status_id !=5 and UpdateDate BETWEEN '"+this_month_first+"' and '"+this_month_last+"' GROUP BY author_name, problem_type;")
    count_error_num = cursor3.fetchall()
    error_info_join_raw = get_problem_num(count_error_num)
    error_info_join = sorted(error_info_join_raw.items(),key = lambda k:k[1],reverse=True)
    name_list = [val[0] for val in error_info_join]
    error_count_num = [val[1] for val in error_info_join]
    
    ab_list = [val["AB"] for val in error_count_num]
    cd_list = [val["CD"] for val in error_count_num]


 
    c['author_name_list'] = author_name_list
    c['update_num_list'] = update_num_list
    c['Principal_list'] = Principal_list
    c['vir_pro_num_list'] = vir_pro_num_list
    c['name_list'] = name_list
    c['ab_list'] = ab_list
    c['cd_list'] = cd_list
    c['month_tag'] = datetime.datetime.strptime(this_month_first,"%Y-%m-%d").date().strftime("%Y年%m月 %d日")+" 至 "+datetime.datetime.strptime(this_month_last,"%Y-%m-%d").date().strftime("%Y年%m月 %d日")
       
    return render_to_response(out_path+'.html',context_instance=c)







