# encoding: utf-8#
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.admin.sites import AdminSite
from django.utils.translation import ugettext as _, ugettext_lazy

from xadmin import views
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction
from .models import Envi_Relation,Envi_Detail
import xadmin


class Envi_RelationAdmin(object):
    list_export = ('xlsx',)
    reversion_enable = True
    
    field =  ('AppID_Source', 'AppID_Target')
    #列表页，列表顶部显示的字段名称
    list_display = ('AppID_Source', 'AppID_Target')
    #列表页出现搜索框，参数是搜索的域
    search_fields = ('AppID_Source', 'AppID_Target')
    #右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    list_filter = ('AppID_Source', 'AppID_Target')
    #自然是排序所用了，减号代表降序排列
    ordering = ('AppID_Source',)
    #表格列表可编辑
    
    list_editable = ('AppID_Source', 'AppID_Target')
   
    
    
       
#将Author模块和管理类绑定在一起，注册到后台管理
xadmin.site.register(Envi_Relation, Envi_RelationAdmin)
