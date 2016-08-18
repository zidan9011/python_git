# encoding: utf-8#
from fileupload.models import SysConfInfo,VerConfInfo,SysDataMineInfo
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.admin.sites import AdminSite
from django.utils.translation import ugettext as _, ugettext_lazy
from .models import *
#怎样自定义列表页面？
from xadmin import views
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction
import xadmin
import modelclone
from django.utils.dateformat import time_format
from django.conf.locale.zh_CN import formats as cn_formats
cn_formats.DATETIME_FORMAT="Y/M/d"
cn_formats.DATE_FORMAT="Y/M/d"
cn_formats.SHORT_DATE_FORMAT="Y/M/d"
cn_formats.SHORT_DATETIME_FORMAT="Y/M/d"

class NameMapAdmin(object):
    list_export = ('xlsx',)
    reversion_enable = True
    actions = ['delete_selected']
    field =  ('rawname', 'mapname')
    #列表页，列表顶部显示的字段名称
    list_display = ('rawname', 'mapname')
    #列表页出现搜索框，参数是搜索的域
    search_fields = ('rawname', 'mapname')
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('rawname', 'mapname')
    #自然是排序所用了，减号代表降序排列
    ordering = ('rawname',)
    #表格列表可编辑
    
    list_editable = ('rawname', 'mapname')
    
    def get_actions(self, request):
        actions = super(NameMapAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    def delete_selected(self, request, obj):
        obj.all().delete()
        tmp_info = NamemapInfo()#更新namemapinfo
        tmp_info.refresh_sys_info()
    
    delete_selected.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")
       
#将Author模块和管理类绑定在一起，注册到后台管理
xadmin.site.register(NameMap, NameMapAdmin)


class DateExchangeAdmin(object):
    list_export = ('xlsx',)
    reversion_enable = True
    actions = ['delete_selected']
    #列表页，列表顶部显示的字段名称
    fields  = ('publisher','subscriber','service_num',
                    'service_system','main_body','data_entity',
                    'data_entity_type','service_name','mep',
                    'ispublic','other_interface_num','interface_name',
                    'interface_num','merge_suggest','update_time',
                    'update_num','bi_service_number',
                    'exchange_method')
    list_display = ('publisher','subscriber','service_num',
                    'service_system','main_body','data_entity',
                    'data_entity_type','service_name','mep',
                    'ispublic','other_interface_num','interface_name',
                    'interface_num','merge_suggest','update_time',
                    'update_num','bi_service_number',
                    'exchange_method')
    #列表页出现搜索框，参数是搜索的域
    search_fields = ('publisher','subscriber','service_num',
                    'service_system','main_body','data_entity',
                    'data_entity_type','service_name','mep',
                    'ispublic','other_interface_num','interface_name',
                    'interface_num','merge_suggest','update_time',
                    'update_num','bi_service_number',
                    'exchange_method')
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('publisher','subscriber','service_num',
                    'service_system','main_body','data_entity',
                    'data_entity_type','service_name','mep',
                    'ispublic','other_interface_num','interface_name',
                    'interface_num','merge_suggest','update_time',
                    'update_num','bi_service_number',
                    'exchange_method')
    #自然是排序所用了，减号代表降序排列
    ordering = ('publisher',)
    #表格列表可编辑
    
    list_editable = ['publisher','subscriber','service_num',
                    'service_system','main_body','data_entity',
                    'data_entity_type','service_name','mep',
                    'ispublic','other_interface_num','interface_name',
                    'interface_num','merge_suggest','update_time',
                    'update_num','bi_service_number',
                    'exchange_method']
    
    def get_actions(self, request):
        actions = super(DateExchangeAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    def delete_selected(self, request, obj):
        obj.all().delete()
        tmp_info = DataExInfo()#更新dataex_info
        tmp_info.refresh_sys_info()
    
    delete_selected.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")
       
#将Author模块和管理类绑定在一起，注册到后台管理
xadmin.site.register(DataExchangeInfo, DateExchangeAdmin)




class SysConfAdmin(object):
    list_export = ('xlsx',)
    reversion_enable = True
    actions = ['delete_selected']
    #列表页，列表顶部显示的字段名称
    fields = ('node_source', 'node_target', 
                    'data_type', 'conn', 'conn_method', 
                    'type')
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
    #表格列表可编辑
    
    list_editable = ['node_source', 'node_target', 
                    'data_type', 'conn', 'conn_method', 
                    'type']
    
    def get_actions(self, request):
        actions = super(SysConfAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    def delete_selected(self, request, obj):
        obj.all().delete()
        tmp_info = SystemInfo()#更新sys_info
        tmp_info.refresh_sys_info()
    
    delete_selected.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")
       
#将Author模块和管理类绑定在一起，注册到后台管理
xadmin.site.register(SysConfInfo, SysConfAdmin)

class SysDataMineAdmin(object):
    #列表页，列表顶部显示的字段名称
    reversion_enable = True
    list_export = ('xls',)    
    list_display = ('node_source', 'node_target', 
                    'from_info')
    #列表页出现搜索框，参数是搜索的域
    search_fields = ('node_source', 'node_target')
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('node_source', 'node_target')
    #自然是排序所用了，减号代表降序排列
    ordering = ('node_source',)

#将Author模块和管理类绑定在一起，注册到后台管理
xadmin.site.register(SysDataMineInfo, SysDataMineAdmin)

class VerConfAdmin(object):
    reversion_enable = True
    list_export = ('xls',)    
    actions = ['delete_selected']
    #列表页，列表顶部显示的字段名称        
    fields = ('main_up_sys_name', 'main_up_sys_version', 
                    'main_up_sys_data_flow', 'relevant_sys_group',
                    'relevant_sys_name', 'relevant_sys_version',
                    'main_relevant_con_if_test', 'main_relevant_con_if_sync',
                    'depend_detail', 'data_interaction_detail','remark_col1')
    list_display = ('main_up_sys_name', 'main_up_sys_version', 
                    'main_up_sys_data_flow', 'relevant_sys_group',
                    'relevant_sys_name', 'relevant_sys_version',
                    'main_relevant_con_if_test', 'main_relevant_con_if_sync',
                    'depend_detail', 'data_interaction_detail','remark_col1')
    #列表页出现搜索框，参数是搜索的域
    search_fields = ('main_up_sys_name', 'main_up_sys_version', 
                    'main_up_sys_data_flow', 'relevant_sys_group',
                    'relevant_sys_name', 'relevant_sys_version',
                    'main_relevant_con_if_test', 'main_relevant_con_if_sync',
                    'depend_detail', 'data_interaction_detail','remark_col1')
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('main_up_sys_name', 'main_up_sys_version', 
                    'main_up_sys_data_flow', 'relevant_sys_group',
                    'relevant_sys_name', 'relevant_sys_version',
                    'main_relevant_con_if_test', 'main_relevant_con_if_sync',
                    'depend_detail', 'data_interaction_detail','remark_col1')
    #自然是排序所用了，减号代表降序排列
    ordering = ('main_up_sys_name',)
    #表格可编辑
    
    list_editable = ['main_up_sys_name', 'main_up_sys_version', 
                    'main_up_sys_data_flow', 'relevant_sys_group',
                    'relevant_sys_name', 'relevant_sys_version',
                    'main_relevant_con_if_test', 'main_relevant_con_if_sync',
                    'depend_detail', 'data_interaction_detail','remark_col1']
    
    def get_actions(self, request):
        actions = super(VerConfAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    
    def delete_selected(self, request, obj):
        obj.all().delete()
        tmp_info = VersionInfo()#更新ver_info
        tmp_info.refresh_sys_info()
    
    delete_selected.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")
#将Author模块和管理类绑定在一起，注册到后台管理
xadmin.site.register(VerConfInfo, VerConfAdmin)

class Report_DetailAdmin(object):
    
    list_export = ('xlsx',)
    reversion_enable = True
    save_as = True
    actions = ['delete_selected']
    list_display = ('SystemName','VersionNum','Main_SysName','Main_VersionNum',
                    'ProjectName','PlanTime','CRType','TestType','ProjectStage',
                    'TestRuns','OverallSchedule',
                    'Reason','ManpowerInput','VersionQuality','Workload','PerformanceTest',
                    'Writter','UpdateDate',)
    #列表页出现搜索框，参数是搜索的域
    search_fields = ('SystemName','VersionNum','Main_SysName','Main_VersionNum',
                    'ProjectName','PlanTime','CRType','TestType','ProjectStage',
                    'TestRuns','OverallSchedule',
                    'Reason','ManpowerInput','VersionQuality','Workload','PerformanceTest',
                    'Writter','UpdateDate')
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('SystemName','VersionNum','Main_SysName','Main_VersionNum',
                    'ProjectName','PlanTime','CRType','TestType','ProjectStage',
                    'TestRuns','OverallSchedule',
                    'Reason','ManpowerInput','VersionQuality','Workload','PerformanceTest',
                    'Writter','UpdateDate',)
    fields = ('SystemName','VersionNum','Main_SysName','Main_VersionNum',
                    'ProjectName','PlanTime','CRType','TestType','ProjectStage',
                    'TestRuns','OverallSchedule',
                    'Reason','ManpowerInput','VersionQuality','Workload','PerformanceTest',
                    'Writter','UpdateDate')
    #自然是排序所用了，减号代表降序排列
    ordering = ('SystemName','VersionNum','Main_SysName','Main_VersionNum',
                    'ProjectName','PlanTime','CRType','TestType','ProjectStage',
                    'TestRuns','OverallSchedule',
                    'Reason','ManpowerInput','VersionQuality','Workload','PerformanceTest',
                    'Writter','UpdateDate')
    #表格列表可编辑
    
    
    list_editable = ['SystemName','VersionNum','Main_SysName','Main_VersionNum',
                    'ProjectName','PlanTime','TestType','ProjectStage',
                    'TestRuns','OverallSchedule',
                    'ManpowerInput','VersionQuality','Workload','CRType','PerformanceTest',
                    'Reason','Writter','UpdateDate',]
    
   
    def save_models(self):
        obj = self.new_obj
        request = self.request
        if len(obj.Writter)==0:
            obj.Writter = request.user.first_name+request.user.last_name
        obj.save()
 
    
    def get_actions(self, request):
        actions = super(Report_DetailAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    
    def delete_selected(self, request, obj):
        obj.all().delete()
        tmp_info = Report_DetailInfo()#更新Report_DetailInfo
        tmp_info.refresh_sys_info()

#注册到后台管理
xadmin.site.register(Report_Detail, Report_DetailAdmin)


class LogEntryAdmin(object):
    reversion_enable = True
    list_export = ('xls',)    
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
xadmin.site.register(LogEntry, LogEntryAdmin)



class GlobalSetting(object):
    #设置base_site.html的Title
    site_title = '系统管理员页面'
    #设置base_site.html的Footer
    site_footer  = '中汇信息技术（上海）有限公司'
    
    
    
    
xadmin.site.register(views.CommAdminView, GlobalSetting)

