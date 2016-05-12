# encoding: utf-8#
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.admin.sites import AdminSite
from cm_vrms_baseline.models import CM_BaseLine_Info,CM_BaseLine_Data_Info
from django.utils.translation import ugettext as _, ugettext_lazy

# Register your models here.
#admin.site.register(CM_BaseLine_Info)
from xadmin import views
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction
from xadmin.views.base import ModelAdminView, filter_hook, csrf_protect_m
import xadmin
class BaseLineAdmin(object):
    list_export = ('xls',)
        
    #actions = ['delete_model_self']
    actions = ['delete_selected']
    #列表页，列表顶部显示的字段名称
    fields = ('AppName', 'AppVersion', 'version_num',
                    'UpdateDate', 'BaseLine', 'environment_fir','PageNumber', 
                    'UppradeTime','UpgradeMan')
    list_display = ('AppName', 'AppVersion', 'version_num',
                    'UpdateDate', 'BaseLine', 'environment_fir','PageNumber', 
                    'UppradeTime','UpgradeMan')
    #列表页出现搜索框，参数是搜索的域
    search_fields = ('AppName', 'AppVersion', 'version_num',
                    'UpdateDate', 'BaseLine', 'environment_fir','PageNumber', 
                    'UppradeTime','UpgradeMan')
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('AppName', 'AppVersion', 'version_num',
                    'UpdateDate', 'BaseLine', 'environment_fir','PageNumber', 
                    'UppradeTime','UpgradeMan')
    #自然是排序所用了，减号代表降序排列
    ordering = ('-UpdateDate',)
    #表格列表可编辑
    list_editable = ['AppName', 'AppVersion', 'version_num',
                    'UpdateDate', 'BaseLine', 'environment_fir','PageNumber', 
                    'UppradeTime','UpgradeMan']
    
    
    def get_actions(self, request):
        actions = super(BaseLineAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            actions.pop('delete_selected')        
        return actions
    
    #def delete_model_self(self, request, obj):
    def delete_selected(self, request, obj):
        obj.all().delete()
        tmp_info = CM_BaseLine_Data_Info()#更新CM_BaseLine_Info
        tmp_info.refresh_sys_info()
    delete_selected.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")
    #reversion_enable = True
    
#将Author模块和管理类绑定在一起，注册到后台管理
xadmin.site.register(CM_BaseLine_Info, BaseLineAdmin)

