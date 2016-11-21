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
from .models import *
import MySQLdb
from django.db import connection,transaction
from fileupload.models import SystemInfo,VersionInfo,SysConfInfo,VerConfInfo,DataExInfo
from django.core.files.base import ContentFile
import time
#from .wikiManager import WikiManager

key_node = ["外汇交易系统","本币交易系统","X-Swap"]

def wiki_index(request):
    '''系统百科详情'''
    cursor1 = connection.cursor() 
    cursor1.execute("SELECT DISTINCT(ChineseName) from cm_vrms_wiki_cm_application;")
    wiki_name = cursor1.fetchall()
    #name_list_raw=[list(val) for val in wiki_name]
    name_list=[val[0] for val in wiki_name]
    c = Context({'STATIC_URL': '/static/'})
    c["node_list_1"] = [val for val in name_list if val in key_node]
    c["node_list_2"] = [val for val in name_list if val not in key_node]
    c["jump_to"] = "application_tree"#指示接下来跳转的位置
    out_path = "wiki_index"
    out_title = "外汇交易中心在建系统"
    c["out_title"] = out_title#指示接下来跳转的位置
    return render_to_response(out_path+'.html',context_instance=c)

def wiki_index_search(request):
    '''百科搜索详情'''
    cursor1 = connection.cursor() 
    cursor1.execute("SELECT DISTINCT(ChineseName) from cm_vrms_wiki_cm_application;")
    wiki_name = cursor1.fetchall()
    name_list_raw=[list(val) for val in wiki_name]
    name_list=[val[0] for val in name_list_raw]
   
    request_node_name = request.GET["query"].encode("utf-8")
    name_list = [val for val in name_list if request_node_name.lower() in val.lower()]
    for val in name_list:
        val = val.encode("utf-8")
    if(len(name_list)) == 0:#若没有查到,则返回全量页面
        return wiki_index(request)
    c = Context({'STATIC_URL': '/static/'})
    c["node_list_1"] = [val for val in name_list if val in key_node]
    c["node_list_2"] = [val for val in name_list if val not in key_node]
    c["jump_to"] = "application_tree"#指示接下来跳转的位置
    out_path = "wiki_index"
    out_title = "外汇交易中心在建系统"
    c["out_title"] = out_title#指示接下来跳转的位置
    return render_to_response(out_path+'.html',context_instance=c)


def as_table(obj_list):
    obj_tmp = obj_list[0]
    #model_name = obj.__class__.__name__
    #verbose_name = obj._meta.verbose_name
    table_upper = '''<table class='table table-bordered table-striped'> <thead><tbody>'''
    result=""
    for i in range(0,len(obj_tmp._meta.fields)):#遍历一个模型内所有的属性
        result += "<tr> <th scope='row'>{}</th>".format(obj_tmp._meta.fields[i].verbose_name)
        for obj in obj_list:
            #inner_val = obj_tmp._meta.fields[i].value_to_string(obj)#将field的值取出来
            attr_name = obj_tmp._meta.fields[i].attname
            if attr_name[-3:] =="_id":#为了展示foreign key的 verbose_name而非id
                attr_name = attr_name[:-3]
            inner_val = str(getattr(obj,attr_name))
            if "img" in attr_name:
                inner_val = "<a class='fancybox' href='/media/{}'><img src='/media/{}'></a>".format(inner_val,inner_val)
            #如果存在choice项的话,将值换成choice中的对应值
            if len(obj_tmp._meta.fields[i].choices)>0:
                for k in range(0,len(obj_tmp._meta.fields[i].choices)):
                    if obj_tmp._meta.fields[i].choices[k][0] == obj_tmp._meta.fields[i].value_to_string(obj):
                        inner_val = obj_tmp._meta.fields[i].choices[k][1]
            if inner_val == "None":
                inner_val = ""
            result += "<td class='text-success'><span class='glyphicon glyphicon-ok' aria-hidden='true'>{}</span></td>" .format(inner_val)
        result += " </tr> "
    for i in range(0,len(obj_tmp._meta.many_to_many)):#遍历一个模型内所有的many_to_many字段
        result += "<tr> <th scope='row'>{}</th>".format(obj_tmp._meta.many_to_many[i].verbose_name)
        for obj in obj_list:
            result += "<td class='text-success'><span class='glyphicon glyphicon-ok' aria-hidden='true'>"
            val_list = []
            for val in getattr(obj,obj._meta.many_to_many[i].column).all():
                if val == "None":
                    val = ""
                val_list.append("{}" .format(val))
            result += "{}</span></td>".format(",".join(val_list))#将值之间用逗号,间隔
        result += "</tr>"
    tabel_end = "</tbody> </table>"
    return "{}{}{}".format(table_upper, result, tabel_end)

def get_content(model_object,foreign_col,foreign_val_list):
    #给定模型、外键字段、外键值,返回具体的html段
    val_set = set()
    for foreign_val in foreign_val_list:
        kwargs = { foreign_col: foreign_val }
        tmp_list = model_object.objects.filter(**kwargs)
        for tmp_val in tmp_list:
            val_set.add(tmp_val)
    val_list = list(val_set)
    model_name = model_object._meta.object_name#model id
    verbose_name = model_object._meta.verbose_name#model名称
    div_upper = '''<div class='tab-pane fade' id='{}'> <h4>{}</h4>'''.format(model_name, verbose_name)
    div_end = "</div>"
    table_content = "<p>系统该部分还没有数据</p>"
    
    if len(val_list) > 0:
        table_content = as_table(val_list)
    #返回所得字段,以及查询得到的元素
    return "{}{}{}".format(div_upper, table_content, div_end),val_list

def get_overview_info(ChineseName):
    cursor = connection.cursor()
    need_sql = "select a.ChineseName,a.EnglishName,b.DevPM,b.DevCompanyPM,b.TestPM,b.TestLD,b.CMA,b.CMB,c.Remark,c.Remark1,c.ServiceIP ,c.LogicHostname from cm_vrms_wiki_cm_application a,cm_vrms_wiki_cm_application_maintainer b,cm_vrms_wiki_appserver c where a.AppID = b.AppID_id and a.AppID = c.AppID_id and ChineseName = '"+ChineseName+"' "
    cursor.execute(need_sql)
    overview_info = cursor.fetchall()
    table_upper = '''<div class='tab-pane fade' id='CM_Overview'><table class='table table-bordered table-striped'> <thead><tbody>'''
    table_title = "<th>系统名称</th><th>英文简称</th><th>项目经理</th><th>开发联系人</th><th>第三方测试负责人</th><th>测试组长</th><th>UAT环境负责人A</th><th>UAT环境负责人B</th><th>环境类别及版本</th><th>IP地址</th><th>逻辑主机名</th>"
    out_str = ""
    need_out_dict = {}
    for val in overview_info:
        ChineseName,EnglishName,DevPM,DevCompanyPM,TestPM,TestLD,CMA,CMB,Remark,Remark1,ServiceIP,LogicHostname = val
        if Remark1 ==None:
            Remark1 = ""
        key = "\t".join(val[:-4])
        Remark = Remark+Remark1
        if key not in need_out_dict:
            need_out_dict[key] = {}
        if Remark not in need_out_dict[key]:
            need_out_dict[key][Remark] = []
        need_out_dict[key][Remark].append([ServiceIP,LogicHostname])

    for key in need_out_dict:
        value_dict = need_out_dict[key]
        value_list = []
        for remark in value_dict:
            serviceIP_logicHostname_info = value_dict[remark]
            serveice_str = "</br>".join([str(val[0]) for val in serviceIP_logicHostname_info])
            logicHostname_str = "</br>".join([str(val[1]) for val in serviceIP_logicHostname_info])
            value_list.append([remark,serveice_str,logicHostname_str])

        for i in range(0,len(value_list)):
            if i == 0:
                key_fileds = key.split("\t")
                row_span = len(value_list)
                td_str = "<td style='vertical-align: inherit;' rowspan='"+str(row_span)+"'>{}</td>"
                format_str =  "<tr>"+td_str*len(key_fileds)+"<td  style='vertical-align: inherit'>{}</td>"*len(value_list[i])+"</tr>"
                tmp_out_list = key_fileds+value_list[i]
                out_str += format_str.format(*tmp_out_list)
            else:
                format_str =  "<tr>"+"<td>{}</td>"*len(value_list[i])+"</tr>"
                out_str += format_str.format(*value_list[i])
        #format_str =  "<tr>"+"<td>{}</td>"*len(val)+"</tr>"
        #out_str += format_str.format(*val)
    #该项目版本历次升级信息的详情展示
    out_str = out_str.encode("utf-8")
    tabel_end = "</tbody> </table></div>"
    return "{}{}{}{}".format(table_upper, table_title, out_str, tabel_end)

def application_tree(request):
    #返回树状图
    tmp_request = request.path.rstrip("/")
    request_node_name = tmp_request.replace("/application_tree_","").encode("utf-8")

    wikiContent = wiki_manager.get_wiki_content(request_node_name)
    table_content = wikiContent.get_content_list()
    
    c = Context({'STATIC_URL': '/static/'})
    c["source_name"] = request_node_name
    c["table_content1"] = table_content[0]
    c["table_content2"] = table_content[1]
    c["table_content3"] = table_content[2]
    c["table_content4"] = table_content[3]
    c["table_content5"] = table_content[4]
    c["table_content6"] = table_content[5]
    c["table_content7"] = table_content[6]
    c["table_content8"] = table_content[7]
    c["table_content9"] = table_content[8]
    c["table_content10"] = table_content[9]
    c["table_content11"] = table_content[10]
    c["table_content12"] = table_content[11]
    c["table_content13"] = table_content[12]
    c["table_content14"] = table_content[13]
    c["table_content15"] = table_content[14]
    c["table_content16"] = table_content[15]
    c["table_content17"] = table_content[16]
    c["table_content18"] = table_content[17]
    c["table_content19"] = table_content[18]
    c["table_content20"] = table_content[19]
    c["table_content21"] = table_content[20]
    c["table_content22"] = table_content[21]
    c["table_content23"] = table_content[22]
    c["table_content_cluser"] = table_content[23]
    c["table_content_img"] = table_content[24]
    c["table_content_mount"] = table_content[25]
    c["table_content_conf_item"] = table_content[26]
    c["table_content_License"] = table_content[27]
    c["table_content_LB"] = table_content[28]
    c["table_content_LB_member"] = table_content[29]
    c["table_overview"] = table_content[30]

    out_path = "application_tree"    
    return render_to_response(out_path+'.html',context_instance=c)
        
        
def as_table_lic(obj_list):
    obj_tmp = obj_list[0]
    table_upper = '''<table class='table table-bordered table-striped'> <thead><tbody>'''
    result="<tr> "
    for i in range(0,len(obj_tmp._meta.fields)):#遍历一个模型内所有的属性
        result += "<th scope='col'>{}</th>".format(obj_tmp._meta.fields[i].verbose_name)
    result += " </tr> "
    
    for obj in obj_list:
        result += " <tr> "
        for i in range(0,len(obj_tmp._meta.fields)):#遍历一个模型内所有的属性
            
            inner_val = obj_tmp._meta.fields[i].value_to_string(obj)#将field的值取出来
                    
            result += "<td class='text-success'><span class='glyphicon glyphicon-ok' aria-hidden='true'>{}</span></td>" .format(inner_val)
        result += " </tr> "
    tabel_end = "</tbody> </table>"
    return "{}{}{}".format(table_upper, result, tabel_end)


def alert_info(request):
    #license过期报警提醒
    out_path = "alert_info"
    c = Context({'STATIC_URL': '/static/'})
    alert_day = (datetime.datetime.now() + datetime.timedelta(days = 3))#将时间拉倒三天后
    need_alert_lists = License.objects.filter(DueDate__lte=alert_day)#将所有小于三天后时间的object取出来
    if len(need_alert_lists) > 0:
        c["message"] = "有license即将过期"
        c["table_content"] = as_table_lic(need_alert_lists)
 
    return render_to_response(out_path+'.html',context_instance=c)



        

