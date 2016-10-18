# encoding: utf-8#
from test_report.models import *
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.admin.sites import AdminSite
from django.utils.translation import ugettext as _, ugettext_lazy

from xadmin import views
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction
from xadmin.views.base import ModelAdminView, filter_hook, csrf_protect_m
import xadmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from reversion.models import Revision, Version
from .models import  *


class UAT_SysNameAdmin(object):
    list_display = ('ProjectGroup','SysName','EngName','EngFullName',)
    #列表页出现搜索框，参数是搜索的域
   
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('ProjectGroup','SysName','EngName','EngFullName',)
    fields = ('ProjectGroup','SysName','EngName','EngFullName',)
    #自然是排序所用了，减号代表降序排列
    ordering = ('ProjectGroup',)
    #表格列表可编辑
    
    list_editable = ['ProjectGroup','SysName','EngName','EngFullName',]
    reversion_enable = True
#注册到后台管理
xadmin.site.register(UAT_SysName, UAT_SysNameAdmin)


class UAT_MaintainerAdmin(object):
    list_display = ('ProjectGroup','ProjectManager','SysName','EngName',
                    'TestPM','TestLD','DevCompanyPM','UATA',
                    'UATB','SimDeployA','SimDeployB','Maintenance',
                    'DevA','DevB',)
    #列表页出现搜索框，参数是搜索的域
   
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('ProjectGroup','ProjectManager','SysName','EngName',
                    'TestPM','TestLD','DevCompanyPM','UATA',
                    'UATB','SimDeployA','SimDeployB','Maintenance',
                    'DevA','DevB',)
    fields = ('ProjectGroup','ProjectManager','SysName','EngName',
                    'TestPM','TestLD','DevCompanyPM','UATA',
                    'UATB','SimDeployA','SimDeployB','Maintenance',
                    'DevA','DevB',)
    #自然是排序所用了，减号代表降序排列
    ordering = ('ProjectGroup',)
    #表格列表可编辑
    
    list_editable = ['ProjectGroup','ProjectManager','SysName','EngName',
                    'TestPM','TestLD','DevCompanyPM','UATA',
                    'UATB','SimDeployA','SimDeployB','Maintenance',
                    'DevA','DevB',]
    reversion_enable = True
#注册到后台管理
xadmin.site.register(UAT_Maintainer, UAT_MaintainerAdmin)


class UAT_ContactAdmin(object):
    list_display = ('Name','Company','Email','Phone',
                    'Tel','Work','Remark',)
    #列表页出现搜索框，参数是搜索的域
   
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('Name','Company','Email','Phone',
                   'Tel','Work','Remark',)
    fields = ('Name','Company','Email','Phone',
              'Tel','Work','Remark',)
    #自然是排序所用了，减号代表降序排列
    ordering = ('Name',)
    #表格列表可编辑
    
    list_editable = ['Name','Company','Email','Phone',
                    'Tel','Work','Remark',]
    reversion_enable = True
#注册到后台管理
xadmin.site.register(UAT_Contact, UAT_ContactAdmin)


class UAT_SYSinfoAdmin(object):
    list_display = ('SysName','EnvType','IP','ServerType',
                    'SysDbType','Scale',)
    #列表页出现搜索框，参数是搜索的域
   
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('SysName','EnvType','IP','ServerType',
                    'SysDbType','Scale',)
    fields = ('SysName','EnvType','IP','ServerType',
              'SysDbType','Scale',)
    #自然是排序所用了，减号代表降序排列
    ordering = ('SysName',)
    #表格列表可编辑
    
    list_editable = ['SysName','EnvType','IP','ServerType',
                     'SysDbType','Scale',]
    reversion_enable = True
#注册到后台管理
xadmin.site.register(UAT_SYSinfo, UAT_SYSinfoAdmin)
    

    
    