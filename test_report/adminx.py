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
from fileupload.models import  *

class SysName_InfoAdmin(object):
    list_display = ('SysName',)
    #列表页出现搜索框，参数是搜索的域
   
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('SysName',)
    fields = ('SysName',)
    #自然是排序所用了，减号代表降序排列
    ordering = ('SysName',)
    #表格列表可编辑
    
    list_editable = ['SysName',]
    reversion_enable = True
#注册到后台管理
xadmin.site.register(SysName_Info, SysName_InfoAdmin)
    

    
    