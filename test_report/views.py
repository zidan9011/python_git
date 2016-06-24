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
def test_report_index(request):
    ProjectStage_map_info = {'xqfx':'需求分析','ylsj':'用例设计','uat1jd':'UAT1阶段','xtcs':'系统测试','yslc':'验收流程','ysjd':'验收阶段','mnlc':'模拟流程','mnjd':'模拟阶段','mncs':'模拟测试','mnwc':'模拟完成','scsx':'生产上线','':''}
    OverallSchedule_map_info = {'zc':'正常','yq':'延期','zt':'暂停','zf':'作废','':''}
    c = Context({'STATIC_URL': '/static/'})
    out_path = "test_report_index"  
    str_need_date_time_start = ""
    str_need_date_time_end = ""   
    try:
        str_need_date_time_start = request.GET["query1"].encode("utf-8")#获取搜索框中的时间
        str_need_date_time_end = request.GET["query2"].encode("utf-8")#获取搜索框中的时间
    except:
        str_need_date_time_start = (datetime.datetime.now()-datetime.timedelta(days=7)).strftime("%Y-%m-%d")
        str_need_date_time_end = datetime.datetime.now().strftime("%Y-%m-%d")
        
    cursor1 = connection.cursor() 
    cursor1.execute("select PlanTime, concat(Main_SysName, Main_VersionNum), OverallSchedule, projectStage, count(case when TestType='sjlc' then TestType end) AS testtype1, count(case when TestType='wyxlc' then TestType end) AS testtype2 from test_report_report_detail  GROUP BY Main_SysName,Main_VersionNum HAVING  PlanTime BETWEEN '"+str_need_date_time_start+"' and '"+str_need_date_time_end+"' order by PlanTime ;")
    report_result = cursor1.fetchall()
    need_out_list = ""
    for val in report_result:
        PlanTime,Main_SysName_ver,OverallSchedule,projectStage,testtype1,testtype2 = val
        projectStage=ProjectStage_map_info[projectStage]
        OverallSchedule=OverallSchedule_map_info[OverallSchedule]
        if OverallSchedule=='正常':
            tab_color='success'
        elif OverallSchedule=='暂停':
            tab_color = 'active'
        elif OverallSchedule=='延期':
            tab_color = 'warning'
        else :
            tab_color = 'active'
            
        
        need_out_list+="<tr class='{}'><td>{}</td><td><a href='/test_report_node/'>{}</a></td><td>{}</td><td>{}</td><td>{}个</td><td>{}个</td></tr>".format(tab_color,PlanTime,Main_SysName_ver,OverallSchedule,projectStage,testtype1,testtype2)
    print need_out_list
        
    c["need_out_list"] = need_out_list
    return render_to_response(out_path+'.html',context_instance=c)


def test_report_node(request):
    c = Context({'STATIC_URL': '/static/'})
    out_path = "test_report_node"  
    return render_to_response(out_path+'.html',context_instance=c)


def test_report_bar(request):
    c = Context({'STATIC_URL': '/static/'})
    out_path = "test_report_bar"  
    return render_to_response(out_path+'.html',context_instance=c)


def test_report_charts(request):
    c = Context({'STATIC_URL': '/static/'})
    out_path = "test_report_charts"  
    return render_to_response(out_path+'.html',context_instance=c)
