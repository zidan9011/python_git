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
from .models import *
from fileupload.models import *
test_type_map_info = {'主系统':'zxt','升级联测':'sjlc','无影响联测':'wyxlc','未回复':'whf','':''}
word_test_type_map = dict([[test_type_map_info[val],val] for val in test_type_map_info]) 
ProjectStage_map_info = {'测试准备':'cszb','UAT1测试':'uat1cs','UAT1完成':'uat1wc','验收流程':'yslc','验收测试':'yscs','模拟流程':'mnlc','模拟测试':'mncs','模拟完成':'mnwc','已上线':'ysx','':'','NA':'NA'}
word_projectStage_map = dict([[ProjectStage_map_info[val],val] for val in ProjectStage_map_info])
OverallSchedule_map_info = {'正常':'zc','延期':'yq','暂停':'zt','作废':'zf','NA':'NA','':''}
word_overallschedule_map = dict([[OverallSchedule_map_info[val],val] for val in OverallSchedule_map_info])
ManpowerInput_map_info = {'人力紧张':'rljz','人力充足':'rlcz','人力不足':'rlbz','':'','NA':'NA'}
word_manpowerInput_map = dict([[ManpowerInput_map_info[val],val] for val in ManpowerInput_map_info])
VersionQuality_map_info = {'质量一般':'zlyb','质量较好':'zljh','质量较差':'zljc','':'','NA':'NA'}
word_versionquality_map = dict([[VersionQuality_map_info[val],val] for val in VersionQuality_map_info])
Workload_map_info = {'超签报':'cqb','正常':'zc','超采购':'ccg','':'','NA':'NA'}    
word_workload_map = dict([[Workload_map_info[val],val] for val in Workload_map_info])

node_symbol = {'主系统':"circle",'升级联测':"circle",'无影响联测':"rectangle",'未回复':"diamond",}
category_number = {"正常":"0","延期":"1","暂停":"2","作废":"3","NA":"4"}
node_projectstage_node_val_map = {'测试准备':'1','UAT1测试':'2','UAT1完成':'3','验收流程':'4','验收测试':'5','模拟流程':'6','模拟测试':'7','模拟完成':'8','已上线':'9'}


testreport_info = Report_DetailInfo()

def test_report_index(request):
    c = Context({'STATIC_URL': '/static/'})
    out_path = "test_report_index"  
    str_need_date_time_start = ""
    str_need_date_time_end = ""   
    try:
        str_need_date_time_start = request.GET["query1"].encode("utf-8")#获取搜索框中的时间
        str_need_date_time_end = request.GET["query2"].encode("utf-8")#获取搜索框中的时间
    except:
        
        str_need_date_time_start = ( datetime.datetime.now() + datetime.timedelta(0 - datetime.datetime.now().weekday())).strftime("%Y-%m-%d")
        #str_need_date_time_end = (datetime.datetime.now()+datetime.timedelta(days=7)).strftime("%Y-%m-%d")
        str_need_date_time_end = ( datetime.datetime.now() + datetime.timedelta(6 - datetime.datetime.now().weekday())).strftime("%Y-%m-%d")
        
    cursor1 = connection.cursor() 
    cursor1.execute("select tb2.PlanTime, CONCAT(tb1.Main_SysName,tb1.Main_VersionNum),tb2.OverallSchedule,tb2.ProjectStage, count(case when tb1.TestType='sjlc' then tb1.TestType end) AS testtype1, count(case when tb1.TestType='wyxlc' then tb1.TestType end) AS testtype2 from test_report_report_detail tb1  LEFT JOIN test_report_report_detail tb2 ON tb1.Main_SysName=tb2.Main_SysName and tb1.Main_VersionNum=tb2.Main_VersionNum where tb2.TestType='zxt' GROUP BY tb1.Main_SysName,tb1.Main_VersionNum HAVING   PlanTime BETWEEN '"+str_need_date_time_start+"' and '"+str_need_date_time_end+"' order by tb2.PlanTime ;")
    report_result = cursor1.fetchall()
    need_out_list = ""
    for val in report_result:
        PlanTime,Main_SysName_ver,OverallSchedule,projectStage,testtype1,testtype2 = val
        projectStage=word_projectStage_map.get(projectStage,"")
        OverallSchedule=word_overallschedule_map.get(OverallSchedule,"")
        if OverallSchedule=='正常':
            tab_color='success'
        elif OverallSchedule=='暂停':
            tab_color = 'active'
        elif OverallSchedule=='延期':
            tab_color = 'warning'
        else :
            tab_color = 'active'
            
        
        need_out_list+="<tr class='{}'><td>{}</td><td><a href='/test_report_node_{}/'>{}</a></td><td>{}</td><td>{}</td><td>{}个</td><td>{}个</td></tr>".format(tab_color,PlanTime,Main_SysName_ver,Main_SysName_ver,OverallSchedule,projectStage,testtype1,testtype2)
    
        
    c["need_out_list"] = need_out_list
    return render_to_response(out_path+'.html',context_instance=c)


def test_report_node(request):
    report_info = testreport_info.sys_info
    c = Context({'STATIC_URL': '/static/'})
    out_path = "test_report_node" 
    request_node_name_version = request.path[:-1].replace("/test_report_node_","").encode("utf-8")
    try:
        print request_node_name_version
        request_node_name = request_node_name_version.split("V")[0]
        request_node_version = "V"+request_node_name_version.split("V")[1]
    except:
        return HttpResponseRedirect('/test_report_index/')#重定向到版本页之初
    
    node_info = {}
    if request_node_name in report_info:
        if request_node_version in report_info[request_node_name]:
            node_info = report_info[request_node_name][request_node_version]
        else:
            return HttpResponseRedirect('/test_report_node/')#重定向到某个系统具体版本页之初
    else:
        return HttpResponseRedirect('/test_report_node/')#重定向到版本页之初
    
    
    #test_type_map_info = {'主系统':'zxt','升级联测':'sjlc','无影响联测':'wyxlc','未回复':'whf','':''}
    #ProjectStage_map_info = {'需求分析':'xqfx','用例设计':'ylsj','UAT1阶段':'uat1jd','系统测试':'xtcs','验收流程':'yslc','验收阶段':'ysjd','模拟流程':'mnlc','模拟阶段':'mnjd','模拟测试':'mncs','模拟完成':'mnwc','生产上线':'scsx','':''}
    #OverallSchedule_map_info = {'正常':'zc','延期':'yq','暂停':'zt','作废':'zf','':''}
    #ManpowerInput_map_info = {'人力紧张':'rljz','人力充足':'rlcz','人力不足':'rlbz','':''}
    #VersionQuality_map_info = {'质量一般':'zlyb','质量较好':'zljh','质量较差':'zljc','':''}
    #Workload_map_info = {'超签报工作量':'cqbgzl','正常':'zc','未立项':'wlx','':''}    

    #主系统：圆形'circle'；升级联测：圆形'circle'；无影响联测：矩形'rectangle'；未回复：菱形 'diamond'
    #正常:0;延期:1;暂停:2;作废:3
    node_table_info_list = []#寄存每个node对应的table信息
    target_node_info = []#寄存节点信息
    link_info = []#寄存边信息
    node_projectstage_node_info = []#寄存柱状图节点信息
    node_projectstage_node_val = []#寄存柱状图节点值信息
    source_node_info = request_node_name+request_node_version
    
    
    for info in node_info:
        SystemName,VersionNum,ProjectName,PlanTime,CRType,TestType,ProjectStage,TestRuns,OverallSchedule,Reason,ManpowerInput,VersionQuality,Workload,PerformanceTest,Writter,UpdateDate = info.split("\t")
        TestType = word_test_type_map.get(TestType,"")
        ProjectStage = word_projectStage_map.get(ProjectStage,"")#转成中文
        OverallSchedule = word_overallschedule_map.get(OverallSchedule,"")#转成中文
        VersionQuality = word_versionquality_map.get(VersionQuality,"")
        ManpowerInput = word_manpowerInput_map.get(ManpowerInput,"")
        Workload = word_workload_map.get(Workload,"")
        
        #"<tr><th>目前项目阶段</th><td>模拟流程</td><th>项目质量</th><td>质量一般</td></tr><tr><th>项目测试工作量投入情况</th><td>超签报工作量</td><th>人力投入情况</th><td>人力充足</td></tr><tr><th >具体原因</th><td colspan=3>因为项目计划拖长导致测试工作量超出签报工作量，已和各方确认在1.1版本的签报补足工作量。</td></tr>"
        #ProjectStage模拟流程,VersionQuality质量一般,Workload超签报工作量,ManpowerInput人力充足,具体原因
        #format的输入:ProjectStage,VersionQuality,Workload,ManpowerInput,Reason
        tmp_node = SystemName+VersionNum
        if ProjectStage!="NA":
            node_projectstage_node_info.append(tmp_node)#寄存柱状图节点信息
            node_projectstage_node_val.append(node_projectstage_node_val_map.get(ProjectStage,"0"))#寄存柱状图节点值信息
        node_table_info_str = "<tr><th>目前项目阶段</th><td>{}</td><th>项目质量</th><td>{}</td></tr><tr><th>项目测试工作量投入情况</th><td>{}</td><th>人力投入情况</th><td>{}</td></tr><tr><th >具体原因</th><td colspan=3>{}</td></tr>".format(ProjectStage,VersionQuality,Workload,ManpowerInput,Reason)
        
        if tmp_node in source_node_info:
            tmp_node_str = "{category:%s, name: '%s', value : 45,symbol:'%s'},"%(category_number.get(OverallSchedule,"0"),source_node_info,'circle')
            target_node_info.append(tmp_node_str)
        elif tmp_node not in source_node_info:
            tmp_node = "{}\\n{}".format(tmp_node,TestType)
            #{category:2, name: '本币CSTPV4.2.77.0\n无影响联测', value : 20,symbol:'star'},
            tmp_node_str = "{category:%s, name: '%s', value : 35,symbol:'%s'},"%(category_number.get(OverallSchedule,"0"),tmp_node,node_symbol.get(TestType,"star"))
            target_node_info.append(tmp_node_str)
            #{source : '外汇交易系统V1.8.5.0', target : 'C-SwapV1.3.0.0\n升级联测', weight :5},
            tmp_link_str = "{source : '%s', target : '%s', weight :5},"%(source_node_info,tmp_node)
            link_info.append(tmp_link_str)
            
        node_table_info_list.append("'{}':'{}',".format(tmp_node,node_table_info_str))
        
    len_num0 = 40*len(node_projectstage_node_info)
    len_num = max(400,len_num0)
            
    c["node_info"] = target_node_info
    c["link_info"] = link_info
    c["node_table_info_list"] = node_table_info_list
    c["node_projectstage_node_info"] = node_projectstage_node_info
    c["node_projectstage_node_val"] = node_projectstage_node_val
    c["len_num"]=len_num
    
    return render_to_response(out_path+'.html',context_instance=c)


def test_report_bar(request):
    c = Context({'STATIC_URL': '/static/'})
    out_path = "test_report_bar"  
    return render_to_response(out_path+'.html',context_instance=c)


def test_report_charts(request):
    c = Context({'STATIC_URL': '/static/'})
    cursor1 = connection.cursor() 
    cursor1.execute("select count(id),OverallSchedule from test_report_report_detail group by OverallSchedule ORDER BY OverallSchedule;")
    overallschedule_result = cursor1.fetchall()
    overallschedule_data=[]
    overallschedule_namedata=[]
    for val in overallschedule_result:
        overallschedule_num,overallschedule_name = val
        overallschedule_name = word_overallschedule_map.get(overallschedule_name,"")
       
        if (overallschedule_name!="") and (overallschedule_name!="NA") :
            
            overallschedule_data.append(overallschedule_num)
            overallschedule_namedata.append(overallschedule_name)
        
    cursor2 = connection.cursor() 
    cursor2.execute("select count(id),VersionQuality from test_report_report_detail group by VersionQuality ORDER BY VersionQuality;")
    versionquality_result = cursor2.fetchall()
    versionquality_data=[]
    versionquality_namedata=[]
    for val in versionquality_result:
        versionquality_num,versionquality_name = val
        versionquality_name = word_versionquality_map.get(versionquality_name,"")
        
        if (versionquality_name!="") and (versionquality_name!="NA") :
            versionquality_data.append(versionquality_num)
            versionquality_namedata.append(versionquality_name)
        
    cursor3 = connection.cursor() 
    cursor3.execute("select count(id),ManpowerInput from test_report_report_detail group by ManpowerInput ORDER BY ManpowerInput;")
    manpowerinput_result = cursor3.fetchall()
    manpowerinput_data=[]
    manpowerinput_namedata=[]
    for val in manpowerinput_result:
        manpowerinput_num,manpowerinput_name = val
        manpowerinput_name = word_manpowerInput_map.get(manpowerinput_name,"")
       
        if (manpowerinput_name!="") and (manpowerinput_name!="NA") :
            manpowerinput_data.append(manpowerinput_num)
            manpowerinput_namedata.append(manpowerinput_name)
        
    cursor4 = connection.cursor() 
    cursor4.execute("select count(id),Workload from test_report_report_detail group by Workload ORDER BY Workload;")
    workload_result = cursor4.fetchall()
    workload_data=[]
    workload_namedata=[]
    for val in workload_result:
        workload_num,workload_name = val
        workload_name = word_workload_map.get(workload_name,"")
     
        if (workload_name!="") and (workload_name!="NA") :
            workload_data.append(workload_num)
            workload_namedata.append(workload_name)
        
    cursor5 = connection.cursor() 
    cursor5.execute("select count(id),ProjectStage from test_report_report_detail group by ProjectStage ORDER BY ProjectStage;")
    projectstage_result = cursor5.fetchall()
    projectstage_namedata = []
    projectstage_numdata=[]
    for val in projectstage_result:
        projectstage_num,projectstage_name = val
        projectstage_name = word_projectStage_map.get(projectstage_name,"")
        
        if (projectstage_name!="") and (projectstage_name!="NA") :
            projectstage_namedata.append(projectstage_name)
            projectstage_numdata.append(projectstage_num)
        
    
    out_path = "test_report_charts"  
    c['overallschedule_data'] = overallschedule_data
    c['overallschedule_namedata']=overallschedule_namedata
    c['versionquality_data'] = versionquality_data
    c['versionquality_namedata']=versionquality_namedata
    c['manpowerinput_data'] = manpowerinput_data
    c['manpowerinput_namedata']=manpowerinput_namedata
    c['workload_data'] = workload_data
    c['workload_namedata']=workload_namedata
    c['projectstage_namedata']  = projectstage_namedata
    c['projectstage_numdata'] = projectstage_numdata
    
    return render_to_response(out_path+'.html',context_instance=c)
