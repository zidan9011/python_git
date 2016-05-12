# encoding: utf-8
from django.db import models
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your models here.
class CqUatst(models.Model):
    severity = models.CharField(db_column='Severity', max_length=255, blank=True, null=True,verbose_name = '严重程度')  # Field name made lowercase.
    prjno = models.CharField(db_column='PrjNo', max_length=255, blank=True, null=True,verbose_name = '项目编号')  # Field name made lowercase.
    unduplicate_state = models.CharField(max_length=255, blank=True, null=True)
    versionno = models.CharField(db_column='VersionNo', max_length=255, blank=True, null=True,verbose_name = '测试版本号')  # Field name made lowercase.
    dbid = models.FloatField(blank=True, null=True)
    assign_date_old = models.DateTimeField(db_column='Assign_date_old', blank=True, null=True)  # Field name made lowercase.
    impatstart = models.DateTimeField(db_column='Impatstart', blank=True, null=True,verbose_name = '影响开始时间')  # Field name made lowercase.
    itil_id = models.CharField(db_column='ITIL_ID', max_length=255, blank=True, null=True,verbose_name = 'ITIL单号')  # Field name made lowercase.
    record_type = models.CharField(max_length=255, blank=True, null=True)
    impattime = models.CharField(db_column='ImpatTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prjname = models.CharField(db_column='PrjName', max_length=255, blank=True, null=True,verbose_name = '项目名称')  # Field name made lowercase.
    submitdate = models.DateTimeField(db_column='Submitdate', blank=True, null=True,verbose_name = '提交时间')  # Field name made lowercase.
    testenv = models.CharField(db_column='TestEnv', max_length=255, blank=True, null=True,verbose_name = '环境')  # Field name made lowercase.
    check_flag = models.BigIntegerField(db_column='Check_flag', blank=True, null=True)  # Field name made lowercase.
    open_flag = models.BigIntegerField(db_column='Open_flag', blank=True, null=True)  # Field name made lowercase.
    defecttype = models.CharField(db_column='DefectType', max_length=255, blank=True, null=True,verbose_name = '问题原因')  # Field name made lowercase.
    open_date_save = models.CharField(db_column='Open_date_save', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_duplicate = models.BigIntegerField(blank=True, null=True)
    open_date = models.DateTimeField(db_column='Open_date', blank=True, null=True,verbose_name = '打开时间')  # Field name made lowercase.
    validate_date_save = models.DateTimeField(db_column='Validate_date_save', blank=True, null=True)  # Field name made lowercase.
    planfinish = models.DateTimeField(db_column='Planfinish', blank=True, null=True,verbose_name = '计划完成时间')  # Field name made lowercase.
    date_flag = models.BigIntegerField(db_column='Date_flag', blank=True, null=True)  # Field name made lowercase.
    bugtype_1 = models.CharField(db_column='BugType_1', max_length=255, blank=True, null=True,verbose_name = '问题类型1')  # Field name made lowercase.
    assign_date = models.DateTimeField(db_column='Assign_date', blank=True, null=True,verbose_name = '分派时间')  # Field name made lowercase.
    is_active = models.BigIntegerField(blank=True, null=True)
    principal = models.CharField(db_column='Principal', max_length=255, blank=True, null=True,verbose_name = '问题经理')  # Field name made lowercase.
    casystemname = models.CharField(db_column='CaSystemName', max_length=255, blank=True, null=True,verbose_name = '引起问题的系统')  # Field name made lowercase.
    resolution = models.CharField(db_column='Resolution', max_length=255, blank=True, null=True,verbose_name = '解决方案')  # Field name made lowercase.
    actualfinish = models.DateTimeField(db_column='Actualfinish', blank=True, null=True,verbose_name = '实际完成时间')  # Field name made lowercase.
    close_date = models.DateTimeField(db_column='Close_date', blank=True, null=True,verbose_name = '关闭时间')  # Field name made lowercase.
    version = models.BigIntegerField(blank=True, null=True)
    locked_by = models.BigIntegerField(blank=True, null=True)
    id = models.CharField(max_length=255, blank=True, verbose_name = 'ID',primary_key=True)
    analysisresult = models.CharField(db_column='AnalysisResult', max_length=255, blank=True, null=True,verbose_name = '分析结论')  # Field name made lowercase.
    impatend = models.DateTimeField(db_column='Impatend', blank=True, null=True,verbose_name = '影响完成时间')  # Field name made lowercase.
    submitter = models.CharField(db_column='Submitter', max_length=255, blank=True, null=True,verbose_name = '提交人')  # Field name made lowercase.
    actualstart = models.DateTimeField(db_column='Actualstart', blank=True, null=True,verbose_name = '实际开始时间')  # Field name made lowercase.
    headline = models.CharField(db_column='Headline', max_length=255, blank=True, null=True,verbose_name = '问题标题')  # Field name made lowercase.
    validate_date = models.DateTimeField(db_column='Validate_date', blank=True, null=True,verbose_name = '验证时间')  # Field name made lowercase.
    rate = models.CharField(db_column='Rate', max_length=255, blank=True, null=True,verbose_name = '优先级')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True,verbose_name = '问题描述')  # Field name made lowercase.
    resolve_date = models.DateTimeField(db_column='Resolve_date', blank=True, null=True,verbose_name = '解决时间')  # Field name made lowercase.
    resolve_date_save = models.CharField(db_column='Resolve_date_save', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bugtype_2 = models.CharField(db_column='BugType_2', max_length=255, blank=True, null=True,verbose_name = '问题类型2')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True,verbose_name = '状态')  # Field name made lowercase.
    resolve_time_save = models.DateTimeField(db_column='Resolve_time_save', blank=True, null=True)  # Field name made lowercase.
    impactnum = models.CharField(db_column='ImpactNum', max_length=255, blank=True, null=True,verbose_name = '影响人数')  # Field name made lowercase.
    lock_version = models.BigIntegerField(blank=True, null=True)
    check_date = models.DateTimeField(db_column='Check_date', blank=True, null=True,verbose_name = '核对时间')  # Field name made lowercase.
    subsystemname = models.CharField(db_column='SubsystemName', max_length=255, blank=True, null=True,verbose_name = '系统名称')  # Field name made lowercase.
    close_time_save = models.DateTimeField(db_column='Close_time_save', blank=True, null=True)  # Field name made lowercase.
    planstart = models.DateTimeField(db_column='Planstart', blank=True, null=True,verbose_name = '计划开始时间')  # Field name made lowercase.
    sumbit_date = models.DateTimeField(db_column='Sumbit_date', blank=True, null=True)  # Field name made lowercase.
    check_date_save = models.DateTimeField(db_column='Check_date_save', blank=True, null=True)  # Field name made lowercase.
    assign_date_save = models.DateTimeField(db_column='Assign_date_save', blank=True, null=True)  # Field name made lowercase.
    bugtype_3 = models.CharField(db_column='BugType_3', max_length=255, blank=True, null=True,verbose_name = '问题类型3')  # Field name made lowercase.
    open_time_save = models.DateTimeField(db_column='Open_time_save', blank=True, null=True)  # Field name made lowercase.
    owner_old = models.CharField(db_column='Owner_old', max_length=255, blank=True, null=True,verbose_name = '问题分析人姓名')  # Field name made lowercase.
    owner_old = models.CharField(db_column='Owner_old', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cq_uatst'