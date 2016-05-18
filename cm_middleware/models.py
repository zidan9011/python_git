# encoding: utf-8
from django.db import models
from django.core.exceptions import ValidationError
import os
import sys
import datetime
import cm_vrms_wiki.models
reload(sys)

# Create your models here.
class Envi_Detail(models.Model):
    AppID = models.IntegerField(verbose_name = '系统ID')
    AppName = models.CharField(max_length=128, verbose_name = '系统名称')
    EnviName = models.CharField(max_length=64,verbose_name='环境名称')
    IP_Usage = models.CharField(max_length=2056,verbose_name='IP及功能')
    
    def __unicode__(self):
        return "{}\t{}\t{}".format(self.AppID,self.AppName,self.EnviName)
    class Meta:
        db_table = u"cm_middleware_Envi_Detail"
        verbose_name=u"系统环境信息表"
        verbose_name_plural=u"系统环境信息表"
    
class Envi_Relation(models.Model):
    
    AppID_Source = models.ForeignKey(Envi_Detail,related_name ='AppID_Source', verbose_name = '源系统ID')
    AppID_Target = models.ForeignKey(Envi_Detail, related_name ='AppID_Target',verbose_name = '目标系统ID')

    
    def __unicode__(self):
        return "{}\t{}".format(self.AppID_Source,self.AppID_Target)
    class Meta:
        db_table = u"cm_middleware_Envi_Relation"
        verbose_name=u"系统各环境关联关系表"
        verbose_name_plural=u"系统各环境关联关系表"
