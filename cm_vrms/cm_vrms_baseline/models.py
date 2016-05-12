# encoding: utf-8
from django.db import models
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your models here.
def singleton(cls, *args, **kw):
    '''单例实现'''  
    instances = {}  
    def _singleton():  
        if cls not in instances:  
            instances[cls] = cls(*args, **kw)  
        return instances[cls]  
    return _singleton
def parse_version_to_int_list(version_name):
    version_name = version_name.replace("V","")
    ver_str_list = version_name.split(".")
    return [int(val) for val in ver_str_list]

class CM_BaseLine_Subject_Info(models.Model):
    subject = models.CharField(max_length=255,verbose_name = '主题内容')
    raw_id = models.IntegerField()
    status_id = models.IntegerField()
    author_name = models.CharField(blank=True,max_length=255,verbose_name = '指派给')
    work_type = models.CharField(max_length=255,verbose_name = '工作类别')
    start_time = models.CharField(max_length=255,verbose_name = '开始时间')
    due_time = models.CharField(max_length=255,verbose_name = '计划完成时间')
    update_type = models.CharField(max_length=255,verbose_name = '升级类别')
    version_num = models.CharField(max_length=255,verbose_name = '补丁号')
    old_version_num = models.CharField(max_length=255,verbose_name = '升级前版本号')
    publish_version_num = models.CharField(max_length=255,verbose_name = '发布版本号')
    online_version_num = models.CharField(max_length=255,verbose_name = '上线版本号')
    approve_person = models.CharField(max_length=255,verbose_name = '升级审批人')
    environment_fir = models.CharField(max_length=255,default = "",verbose_name = '升级环境（一级）')
    environment_sec = models.CharField(max_length=255,verbose_name = '环境分类（二级）')
    environment_thi = models.CharField(max_length=255,verbose_name = '环境分类（三级）')
    update_date = models.CharField(max_length=255,verbose_name = '升级日期')
    change_content = models.CharField(max_length=255,verbose_name = '变更内容-部署升级')
    update_method = models.CharField(max_length=255,verbose_name = '升级方式')
    db_changed = models.CharField(max_length=255,verbose_name = '是否有数据库变更')
    client_content = models.CharField(max_length=255,verbose_name = '客户端内容')
    base_line_num = models.CharField(max_length=255,verbose_name = '基线号')
    update_book_num = models.CharField(max_length=255,verbose_name = '升级步骤手册页数')
    work_num = models.CharField(max_length=255,verbose_name = '工作量（人天）')
    project = models.CharField(max_length=255,verbose_name = '所属项目群组')
    problem_source = models.CharField(max_length=255,verbose_name = '问题原因')
    problem_type = models.CharField(max_length=255,verbose_name = '问题类型')
    update_reason = models.CharField(max_length=255,verbose_name = '升级原因')
    
    def __unicode__(self):
        return '''{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}'''.format(self.subject,
                         self.work_type,
                         self.start_time,
                         self.due_time,
                         self.update_type,
                         self.version_num,
                         self.old_version_num,
                         self.publish_version_num)
    class Meta:
        db_table = u"cm_vrms_baseline_cm_baseline_subject_info"
        verbose_name=u"报工系统版本基线信息"
        verbose_name_plural=u"报工系统版本基线信息(总)"

class CM_BaseLine_Info(models.Model):
    #AppID=models.IntegerField(verbose_name = '应用系统ID')
    AppName=models.CharField(max_length=100, verbose_name = '应用系统名称')
    raw_id = models.IntegerField()
    status_id = models.IntegerField()
    AppVersion=models.CharField(max_length=100, verbose_name = '应用系统版本号' )
    UpdateDate=models.DateField(verbose_name = '升级时间' )
    BaseLine=models.CharField(max_length=128,blank=True, verbose_name = '代码基线号' )
    PageNumber=models.CharField(max_length=100, blank=True, verbose_name = '升级步骤页数' )
    UppradeTime=models.CharField(max_length=20,blank=True, verbose_name = '工作量' )
    version_num = models.CharField(max_length=255,verbose_name = '补丁号')
    environment_fir = models.CharField(max_length=255,verbose_name = '升级环境（一级）')
    UpgradeMan=models.CharField(blank=True, max_length=100,verbose_name = '指派给' )
    project = models.CharField(max_length=255,verbose_name = '所属项目群组')
    problem_source = models.CharField(blank=True,max_length=255,verbose_name = '问题原因')
    problem_type = models.CharField(max_length=255,verbose_name = '问题类型') 
    update_reason = models.CharField(max_length=255,verbose_name = '升级原因')   
    update_type = models.CharField(max_length=255,verbose_name = '升级类别')  
    def save(self, *args, **kwargs):
        '''重写保存方法'''
        super(CM_BaseLine_Info, self).save(*args, **kwargs) # Call the "real" save() method.
        tmp_info = CM_BaseLine_Data_Info()#更新sys_info
        tmp_info.refresh_sys_info() 
    
    def delete(self, *args, **kwargs):
        #重写删除方法
        super(CM_BaseLine_Info, self).delete(*args, **kwargs) # Call the "real" delete() method.
        tmp_info = CM_BaseLine_Data_Info()#更新sys_info
        tmp_info.refresh_sys_info()                
    
        
    def __unicode__(self):
        return '''{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}'''.format(self.AppName,
                         self.AppVersion,
                         self.UpdateDate,
                         self.BaseLine,
                         self.PageNumber,
                         self.UppradeTime,
                         self.version_num,
                         self.environment_fir,
                         self.UpgradeMan,
                         self.update_reason)
    class Meta:
        db_table = u"cm_vrms_baseline_cm_baseline_info"
        verbose_name=u"版本基线信息"
        verbose_name_plural=u"各系统版本基线表(总)"
@singleton    
class CM_BaseLine_Data_Info(models.Model):
    '''为基线信息'''
    
    def __init__(self):
        self.base_line_info = {}
        self.base_line_info = self.read_baseline_info_from_db()
        
    def read_baseline_info_from_db(self):
        #从数据库中读取conf_info
        bl_info_list = CM_BaseLine_Info.objects.order_by("UpdateDate")
        '''时间由远及近,从去年到今年'''
        ver_baseline_info = {}
        app_version_max = {}#记录四位版本号,每一位版本号的最大值 
            
        for bl_info in bl_info_list:
            AppName=bl_info.AppName.encode("utf-8")
            AppVersion=bl_info.AppVersion.encode("utf-8")
            UpdateDate=bl_info.UpdateDate
            BaseLine=bl_info.BaseLine.encode("utf-8")
            PageNumber=bl_info.PageNumber.encode("utf-8")
            UppradeTime=bl_info.UppradeTime
            UpgradeMan=bl_info.UpgradeMan
            if UpgradeMan:
                UpgradeMan = UpgradeMan.encode("utf-8")
            version_num=bl_info.version_num
            if version_num:
                version_num = version_num.encode("utf-8")
            environment_fir=bl_info.environment_fir
            if environment_fir:
                environment_fir = environment_fir.encode("utf-8")
            if AppName not in ver_baseline_info:
                ver_baseline_info[AppName] = []
            #应用名称    应用版本    升级时间  基线号  升级步骤页数   升级耗时  补丁号 升级环境(一级) 升级操作人
            #AppName,AppVersion,UpdateDate，BaseLine，PageNumber，UppradeTime，version_num,environment_fir,UpgradeMan
            y_index = int("".join(str(UpdateDate).split("-")))
            if AppName not in ver_baseline_info:
                ver_baseline_info[AppName] = []
            #应用名称    应用版本    升级时间  基线号  升级步骤页数   升级耗时  补丁号 升级环境(一级) 升级操作人
            #AppName,AppVersion,UpdateDate，BaseLine，PageNumber，UppradeTime，version_num,environment_fir,UpgradeMan
            ver_baseline_info[AppName].append([AppVersion,UpdateDate,BaseLine,PageNumber,UppradeTime,version_num,environment_fir,UpgradeMan,y_index])
        ver_baseline_info_list = sorted(ver_baseline_info.items(),key = lambda x:len(x[1]))#根据每个系统更新版本的多少来进行排序
        return ver_baseline_info_list
    def refresh_sys_info(self):
        #更新基线信息
        self.base_line_info = self.read_baseline_info_from_db()
        
    def get_extra_data(self,version_info):
        '''返回详细数据,并放在data中,用于前台显示'''
        #应用名称    应用版本    升级时间  基线号  升级步骤页数   升级耗时  补丁号 升级环境(一级) 升级操作人
        #AppName,AppVersion,UpdateDate，BaseLine，PageNumber，UppradeTime，version_num,environment_fir,UpgradeMan
        
        AppVersion,UpdateDate,BaseLine,PageNumber,UppradeTime,version_num,environment_fir,UpgradeMan,y_index = version_info
        return "{value:"+str(y_index)+",应用版本:'"+AppVersion+"',升级时间:'"+str(UpdateDate)+"',基线号:'"+BaseLine+"',升级步骤页数:'"+PageNumber+"',升级耗时:'"+str(UppradeTime)+"',补丁号:'"+version_num+"',升级环境:'"+environment_fir+"',升级操作人:'"+UpgradeMan+"'}"
    def get_tri_datas(self,need_date):
        need_y_index = int("".join(str(need_date).split("-")))
        app_name_list = []
        this_time_data = []
        old_time_data = []
        new_time_data = []
        for app_info in self.base_line_info:
            app_name,app_versions = app_info
            i = 0#防止版本长度为1的系统,不给i赋值
            have_tag = False#该app_name是否被添加进来
            for i in range(len(app_versions)-1):
                if app_versions[i][-1] <= need_y_index and \
                   app_versions[i+1][-1] > need_y_index :
                    '''最普通情况,当前版本的时间小于基线时间,后一个版本的时间大于基线时间'''
                    have_tag = True
                    app_name_list.append(app_name)

                    this_time_data.append(self.get_extra_data(app_versions[i]))#当前时间
                    new_time_data.append(self.get_extra_data(app_versions[i+1]))#后继时间
                    #this_time_data.append(app_versions[i][-1])#当前时间
                    #new_time_data.append(app_versions[i+1][-1])#后继时间
                    if i > 0:#如果不是第一个
                        old_time_data.append(self.get_extra_data(app_versions[i-1]))#前驱时间
                        #old_time_data.append(app_versions[i-1][-1])#前驱时间
                    else:#如果是第一个,则前驱仍为自己
                        old_time_data.append(self.get_extra_data(app_versions[i]))#前驱时间
                        #old_time_data.append(app_versions[i][-1])#前驱时间
            if not have_tag:#如果没有被纳入
                if len(app_versions) == 1:#如果该节点只有1个版本,不会进入上面的循环
                    if app_versions[i][-1] <= need_y_index:
                        app_name_list.append(app_name)
                        this_time_data.append(self.get_extra_data(app_versions[i]))#当前时间
                        new_time_data.append(self.get_extra_data(app_versions[i]))#后继时间  
                        old_time_data.append(self.get_extra_data(app_versions[i]))#前驱时间
                    else:
                        pass#若第一个版本都大于现在的时间,则抛弃该app_name
                else:#若有多个版本                   
                    if app_versions[i+1][-1] <= need_y_index:#说明没有比当前时间大的版本
                        app_name_list.append(app_name)
                        this_time_data.append(self.get_extra_data(app_versions[i+1]))#当前时间
                        new_time_data.append(self.get_extra_data(app_versions[i+1]))#后继时间    
                        old_time_data.append(self.get_extra_data(app_versions[i]))#前驱时间                
                    else:#说明最小值都比当前时间大
                        pass#则不处理,不被吸纳入此次处理的情况
        all_name_this_old_new_info = zip(app_name_list,this_time_data,old_time_data,new_time_data)
        all_name_this_old_new_info = sorted(all_name_this_old_new_info,key = lambda k:int(this_time_data[app_name_list.index(k[0])].split(",")[0].split(":")[1]),reverse=True)#由k[0]这个appname来找寻this_time_data,最后根据this_time_data来排序
        app_name_list,this_time_data,old_time_data,new_time_data = zip(*all_name_this_old_new_info)#反解成tuple list
        return app_name_list,this_time_data,old_time_data,new_time_data
                    
    def select_by_date(self,need_date):
        #从数据库中读取conf_info
        
        bl_info_list = CM_BaseLine_Info.objects.filter(UpdateDate__lte=need_date).order_by("UpdateDate")
        '''时间由远及近,从去年到今年[0-->-1]'''
        ver_baseline_info = {}
        for bl_info in bl_info_list:
            AppName=bl_info.AppName.encode("utf-8")
            AppVersion=bl_info.AppVersion.encode("utf-8")
            UpdateDate=bl_info.UpdateDate
            BaseLine=bl_info.BaseLine.encode("utf-8")
            PageNumber=bl_info.PageNumber.encode("utf-8")
            UppradeTime=bl_info.UppradeTime
            UpgradeMan=bl_info.UpgradeMan.encode("utf-8")
            version_num=bl_info.version_num.encode("utf-8")
            environment_fir=bl_info.environment_fir.encode("utf-8")
            if AppName not in ver_baseline_info:
                ver_baseline_info[AppName] = []
            #应用名称    应用版本    升级时间  基线号  升级步骤页数   升级耗时  补丁号 升级环境(一级) 升级操作人
            #AppName,AppVersion,UpdateDate，BaseLine，PageNumber，UppradeTime，version_num,environment_fir,UpgradeMan
            y_index = int("".join(str(UpdateDate).split("-")))
            if AppName not in ver_baseline_info:
                ver_baseline_info[AppName] = []
            #应用名称    应用版本    升级时间  基线号  升级步骤页数   升级耗时  补丁号 升级环境(一级) 升级操作人
            #AppName,AppVersion,UpdateDate，BaseLine，PageNumber，UppradeTime，version_num,environment_fir,UpgradeMan
            ver_baseline_info[AppName].append([AppVersion,UpdateDate,BaseLine,PageNumber,UppradeTime,version_num,environment_fir,UpgradeMan,y_index])
        ver_baseline_info_list = sorted(ver_baseline_info.items(),key = lambda x:len(x[1]))#根据每个系统更新版本的多少来进行排序
        return ver_baseline_info_list



class CmVrmsBaselineCustomValues(models.Model):
    id = models.IntegerField(primary_key=True)
    customized_type = models.CharField(max_length=30)
    customized_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    value = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_values'

class CmVrmsBaselineUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=255)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'  

class CmVrmsBaselineRequire(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name = 'id')
    issue_id = models.IntegerField(max_length=11,verbose_name = 'issue_id')
    project_name = models.CharField(max_length=255, blank=True, null=True,verbose_name = '项目')
    subject = models.CharField(max_length=255, blank=True, null=True,verbose_name = '主题')
    user_name = models.CharField(max_length=255, blank=True, null=True,verbose_name = '作者')
    emergence = models.CharField(max_length=255, blank=True, null=True,verbose_name = '紧迫程度')
    proposed_department = models.CharField(max_length=255, blank=True, null=True,verbose_name = '提出部门')
    reason = models.CharField(max_length=255, blank=True, null=True,verbose_name = '提出原因')
    due_time = models.CharField(max_length=255, blank=True, null=True,verbose_name = '期望上线时间')
    require_type = models.CharField(max_length=255, blank=True, null=True,verbose_name = '需求类型')
    require_system = models.CharField(max_length=255, blank=True, null=True,verbose_name = '需求实现系统')
    version = models.CharField(max_length=255, blank=True, null=True,verbose_name = '计划上线版本')
    owner = models.CharField(max_length=255, blank=True, null=True,verbose_name = '项目组负责人')
    main_system_name =  models.CharField(max_length=255, blank=True, null=True,verbose_name = '主系统名称')
    main_ver_num =  models.CharField(max_length=255, blank=True, null=True,verbose_name = '主系统版本')

    class Meta:
        managed = False
        db_table = 'require_issue'           

        
class CmVrmsBaselineErrors(models.Model):
    subject = models.CharField(max_length=255)
    raw_id = models.IntegerField()
    status_id = models.IntegerField()
    UpdateDate=models.DateField(verbose_name = '开始时间' )
    project = models.CharField(max_length=255,verbose_name = '所属项目群组')
    problem_source = models.CharField(max_length=255,verbose_name = '问题原因')
    problem_type = models.CharField(max_length=255,verbose_name = '问题类型')
    author_name = models.CharField(max_length=255,verbose_name = '指派给')
    
    def __unicode__(self):
        return "{}\t{}\t{}".format(self.subject,self.UpdateDate,self.EndDate)

    class Meta:
        
        db_table = u"cm_vrms_baseline_errors" 
        
        

class CmVrmsBaselineProjects(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=5000, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    is_public = models.SmallIntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    inherit_members = models.SmallIntegerField()
    project_meeting_rooms = models.CharField(max_length=255, blank=True, null=True)
    project_name_view = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'           


class CmVrmsBaselineIssues(models.Model):
    id = models.IntegerField(primary_key=True)
    tracker_id = models.IntegerField()
    project_id = models.IntegerField()
    subject = models.CharField(max_length=255)
    description = models.CharField(max_length=5000, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField()
    assigned_to_id = models.IntegerField(blank=True, null=True)
    priority_id = models.IntegerField()
    fixed_version_id = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField()
    lock_version = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    done_ratio = models.IntegerField()
    estimated_hours = models.FloatField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    root_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    is_private = models.SmallIntegerField()
    closed_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issues'



class UpdatetimeInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    AppName=models.CharField(max_length=100, verbose_name = '应用系统名称')
    AppVersion=models.CharField(max_length=100, verbose_name = '应用系统版本号' )
    UpdateDate=models.DateField(verbose_name = '升级时间' )
    environment_fir = models.CharField(max_length=255,verbose_name = '升级环境（一级）')

    class Meta:
        
        db_table = 'update_time'

    


