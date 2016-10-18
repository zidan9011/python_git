# encoding: utf-8
from django.db import models
from django.core.exceptions import ValidationError
import os
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

class UAT_SysName(models.Model):
    #UAT环境系统名称总表
    ID = models.AutoField(primary_key=True, verbose_name = 'ID')
    ProjectGroup = models.CharField(max_length=128,  verbose_name = '项目群')
    SysName = models.CharField(max_length=128,  verbose_name = '系统名称')
    EngName = models.CharField(max_length=64, verbose_name = '英文简称')
    EngFullName = models.CharField(max_length=128, verbose_name = '英文全称')
    
    
    def __unicode__(self):
        return "{}".format(self.ID)
    
    class Meta:
        db_table = u"cm_vrms_uat_info_uat_sysname"
        verbose_name=u"UAT环境系统名称总表"
        verbose_name_plural=u"UAT环境系统名称总表"


class UAT_Maintainer(models.Model):
    #UAT环境系统接口人对应表
    ID = models.AutoField(primary_key=True, verbose_name = 'ID')
    ProjectGroup = models.CharField(max_length=128,  verbose_name = '项目群')
    ProjectManager = models.CharField(max_length=64, verbose_name = '项目经理') 
    SysName = models.CharField(max_length=128, verbose_name = '系统名称') 
    EngName = models.CharField(max_length=64, verbose_name = '英文简称')
    TestPM = models.CharField(max_length=32, verbose_name = '测试负责人')
    TestLD = models.CharField(max_length=32, verbose_name = '第三方测试组长')
    DevCompanyPM = models.CharField(max_length=32, verbose_name = '开发联系人')
    UATA  =  models.CharField(max_length=32, verbose_name = 'UAT配置管理员A角')
    UATB  =  models.CharField(max_length=32, verbose_name = 'UAT配置管理员B角')
    SimDeployA = models.CharField(max_length=128, verbose_name = '模拟部署A')
    SimDeployB = models.CharField(max_length=128, verbose_name = '运行交付岗B')
    Maintenance = models.CharField(max_length=64, verbose_name = '维护方')
    DevA = models.CharField(max_length=32, verbose_name = '技术开发部联系人A角')
    DevB = models.CharField(max_length=32, verbose_name = '技术开发部联系人B角')
    
    def __unicode__(self):
        return "{}".format(self.ID)
    
    class Meta:
        db_table = u"cm_vrms_uat_info_uat_maintainer"
        verbose_name=u"UAT环境系统接口人员对应表"
        verbose_name_plural=u"UAT环境系统接口人员对应表"
        
class UAT_Contact(models.Model):
    #UAT环境相关人员联系方式
    ID = models.AutoField(primary_key=True, verbose_name = 'ID')
    Name = models.CharField(max_length=64,  verbose_name = '姓名')
    Company = models.CharField(max_length=64, verbose_name = '所属公司') 
    Email = models.CharField(max_length=64, verbose_name = '邮箱') 
    Phone = models.CharField(max_length=64, verbose_name = '电话')
    Tel = models.CharField(max_length=32, verbose_name = '分机')
    Work = models.CharField(max_length=32, verbose_name = '分工')
    Remark = models.CharField(max_length=128, verbose_name = '备注')
    
    
    def __unicode__(self):
        return "{}".format(self.ID)
    
    class Meta:
        db_table = u"cm_vrms_uat_info_uat_contact"
        verbose_name=u"UAT环境相关人员联系方式"
        verbose_name_plural=u"UAT环境相关人员联系方式"
        
        
class UAT_SYSinfo(models.Model):
    #UAT环境系统IP地址
    Scale_CHOICES = (('Y','是'),('N','否'))
    ID = models.AutoField(primary_key=True, verbose_name = 'ID')
    SysName = models.CharField(max_length=128,  verbose_name = '系统名称')
    EnvType = models.CharField(max_length=64, verbose_name = '环境类别') 
    IP = models.CharField(max_length=128, verbose_name = 'IP地址') 
    ServerType = models.CharField(max_length=64, verbose_name = '服务器类别')
    SysDbType = models.CharField(max_length=128, verbose_name = '系统/数据库版本')
    Scale = models.CharField(choices=Scale_CHOICES,max_length=32, verbose_name = 'UAT和模拟生产机器数是否1:1')
    
    
    def __unicode__(self):
        return "{}".format(self.ID)
    
    class Meta:
        db_table = u"cm_vrms_uat_info_uat_sysinfo"
        verbose_name=u"UAT环境应用系统IP"
        verbose_name_plural=u"UAT环境应用系统IP"
