# encoding: utf-8#
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.admin.sites import AdminSite
from cm_vrms_baseline.models import CM_BaseLine_Info,CM_BaseLine_Data_Info
from django.utils.translation import ugettext as _, ugettext_lazy

# Register your models here.
#admin.site.register(CM_BaseLine_Info)

class BaseLineAdmin(admin.ModelAdmin):
    actions = ['delete_model_self']
    #列表页，列表顶部显示的字段名称
    list_display = ('AppName', 'AppVersion', 
                    'UpdateDate', 'BaseLine', 'PageNumber', 
                    'UppradeTime','UpgradeMan')
    #列表页出现搜索框，参数是搜索的域
    search_fields = ('AppName', 'AppVersion', 
                    'UpdateDate', 'BaseLine', 'PageNumber', 
                    'UppradeTime','UpgradeMan')
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('AppName', 'UpdateDate')
    #自然是排序所用了，减号代表降序排列
    ordering = ('UpdateDate',)
    
    def get_actions(self, request):
        actions = super(BaseLineAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    
    def delete_model_self(self, request, obj):
        obj.all().delete()
        tmp_info = CM_BaseLine_Data_Info()#更新CM_BaseLine_Info
        tmp_info.refresh_sys_info()
    
    delete_model_self.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")
    
#将Author模块和管理类绑定在一起，注册到后台管理
admin.site.register(CM_BaseLine_Info, BaseLineAdmin)

