# encoding: utf-8#
from fileupload.models import SysConfInfo,VerConfInfo,SysDataMineInfo
from django.contrib import admin
from xadmin.util import json
from django.contrib.admin.models import LogEntry
from django.template import loader
from django.utils.html import escape
from django.utils.xmlutils import SimplerXMLGenerator
from django.contrib.admin.sites import AdminSite
from django.utils.translation import ugettext as _, ugettext_lazy
from .models import SystemInfo,VersionInfo,SysConfInfo,VerConfInfo
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.utils.encoding import force_str, smart_unicode
from django.db.models import BooleanField, NullBooleanField
from xadmin.views.list import ALL_VAR
from django.http import HttpResponse
import StringIO
import datetime
import sys
try:
    import xlwt
    has_xlwt = True
except:
    has_xlwt = False

try:
    import xlsxwriter
    has_xlsxwriter = True
except:
    has_xlsxwriter = False
#怎样自定义列表页面？


class SysConfAdmin(admin.ModelAdmin):
    actions = ['delete_model_self']
    #列表页，列表顶部显示的字段名称
    list_display = ('node_source', 'node_target', 
                    'data_type', 'conn', 'conn_method', 
                    'type')
    #列表页出现搜索框，参数是搜索的域
    search_fields = ('node_source', 'node_target', 
                    'data_type', 'conn', 'conn_method', 
                    'type')
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('node_source', 'node_target', 
                    'data_type', 'conn', 'conn_method', 
                    'type')
    #自然是排序所用了，减号代表降序排列
    ordering = ('node_source',)
    def get_actions(self, request):
        actions = super(SysConfAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    def delete_model_self(self, request, obj):
        obj.all().delete()
        tmp_info = SystemInfo()#更新sys_info
        tmp_info.refresh_sys_info()
    
    delete_model_self.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")
    #delete_model.short_description = '新删除'       
#将Author模块和管理类绑定在一起，注册到后台管理
admin.site.register(SysConfInfo, SysConfAdmin)

class SysDataMineAdmin(admin.ModelAdmin):
    #列表页，列表顶部显示的字段名称
    list_display = ('node_source', 'node_target', 
                    'from_info')
    #列表页出现搜索框，参数是搜索的域
    search_fields = ('node_source', 'node_target')
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('node_source', 'node_target')
    #自然是排序所用了，减号代表降序排列
    ordering = ('node_source',)

#将Author模块和管理类绑定在一起，注册到后台管理
admin.site.register(SysDataMineInfo, SysDataMineAdmin)

class VerConfAdmin(admin.ModelAdmin):
    actions = ['delete_model_self']
    #列表页，列表顶部显示的字段名称
    list_display = ('main_up_sys_name', 'main_up_sys_version', 
                    'relevant_sys_name', 'relevant_sys_version')
    #列表页出现搜索框，参数是搜索的域
    search_fields = ('main_up_sys_name', 'main_up_sys_version', 
                    'relevant_sys_name', 'relevant_sys_version')
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('main_up_sys_name', 'main_up_sys_version', 
                    'relevant_sys_name', 'relevant_sys_version')
    #自然是排序所用了，减号代表降序排列
    ordering = ('main_up_sys_name',)

    def get_actions(self, request):
        actions = super(VerConfAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    
    def delete_model_self(self, request, obj):
        obj.all().delete()
        tmp_info = VersionInfo()#更新ver_info
        tmp_info.refresh_sys_info()
    
    delete_model_self.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")
#将Author模块和管理类绑定在一起，注册到后台管理
admin.site.register(VerConfInfo, VerConfAdmin)


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'action_time', 
                    'user', 'content_type',
                    'object_id', 'object_repr',
                    'action_flag')
    #列表页出现搜索框，参数是搜索的域
    search_fields = ('user', 'action_time')
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('user', 'action_time')
    #自然是排序所用了，减号代表降序排列
    ordering = ('-action_time',)
admin.site.register(LogEntry, LogEntryAdmin)

admin.site.index_title = "系统管理员页面"
