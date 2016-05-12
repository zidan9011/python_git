# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class CmVrmsBaselineCmBaselineDataInfo(models.Model):

    class Meta:
        managed = False
        db_table = 'cm_vrms_baseline_cm_baseline_data_info'


class CmVrmsBaselineCmBaselineInfo(models.Model):
    appname = models.CharField(db_column='AppName', max_length=100)  # Field name made lowercase.
    raw_id = models.IntegerField()
    status_id = models.IntegerField()
    appversion = models.CharField(db_column='AppVersion', max_length=100)  # Field name made lowercase.
    updatedate = models.DateField(db_column='UpdateDate')  # Field name made lowercase.
    baseline = models.CharField(db_column='BaseLine', max_length=128)  # Field name made lowercase.
    pagenumber = models.CharField(db_column='PageNumber', max_length=100)  # Field name made lowercase.
    uppradetime = models.CharField(db_column='UppradeTime', max_length=20)  # Field name made lowercase.
    version_num = models.CharField(max_length=255)
    environment_fir = models.CharField(max_length=255)
    upgrademan = models.CharField(db_column='UpgradeMan', max_length=100)  # Field name made lowercase.
    project = models.CharField(max_length=255)
    problem_source = models.CharField(max_length=255)
    problem_type = models.CharField(max_length=255)
    update_reason = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cm_vrms_baseline_cm_baseline_info'


class CmVrmsBaselineCmBaselineSubjectInfo(models.Model):
    subject = models.CharField(max_length=255)
    raw_id = models.IntegerField()
    status_id = models.IntegerField(blank=True, null=True)
    author_name = models.CharField(max_length=255)
    work_type = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255)
    due_time = models.CharField(max_length=255)
    update_type = models.CharField(max_length=255)
    version_num = models.CharField(max_length=255)
    old_version_num = models.CharField(max_length=255)
    publish_version_num = models.CharField(max_length=255)
    online_version_num = models.CharField(max_length=255)
    approve_person = models.CharField(max_length=255)
    environment_fir = models.CharField(max_length=255)
    environment_sec = models.CharField(max_length=255)
    environment_thi = models.CharField(max_length=255)
    update_date = models.CharField(max_length=255)
    change_content = models.CharField(max_length=255)
    update_method = models.CharField(max_length=255)
    db_changed = models.CharField(max_length=255)
    client_content = models.CharField(max_length=255)
    base_line_num = models.CharField(max_length=255)
    update_book_num = models.CharField(max_length=255)
    work_num = models.CharField(max_length=255)
    project = models.CharField(max_length=255)
    problem_source = models.CharField(max_length=255)
    problem_type = models.CharField(max_length=255)
    update_reason = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cm_vrms_baseline_cm_baseline_subject_info'


class CmVrmsBaselineErrors(models.Model):
    subject = models.CharField(max_length=255)
    raw_id = models.IntegerField()
    status_id = models.IntegerField()
    updatedate = models.DateField(db_column='UpdateDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
    project = models.CharField(max_length=255)
    problem_source = models.CharField(max_length=255)
    problem_type = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cm_vrms_baseline_errors'


class CmVrmsWikiApache(models.Model):
    apacheid = models.AutoField(db_column='ApacheID', primary_key=True)  # Field name made lowercase.
    softwareid = models.ForeignKey('CmVrmsWikiSoftware', db_column='SoftwareID_id')  # Field name made lowercase.
    port = models.IntegerField(db_column='Port')  # Field name made lowercase.
    sslport = models.IntegerField(db_column='SSLPort')  # Field name made lowercase.
    docmentroot = models.CharField(db_column='DocmentRoot', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_apache'


class CmVrmsWikiAppserver(models.Model):
    appserverid = models.AutoField(db_column='AppServerID', primary_key=True)  # Field name made lowercase.
    appid = models.ForeignKey('CmVrmsWikiCmApplication', db_column='AppID_id')  # Field name made lowercase.
    deviceid = models.ForeignKey('CmVrmsWikiDevice', db_column='DeviceID_id')  # Field name made lowercase.
    hostname = models.CharField(db_column='HostName', max_length=32)  # Field name made lowercase.
    osname = models.CharField(db_column='OsName', max_length=32)  # Field name made lowercase.
    osversion = models.CharField(db_column='OSVersion', max_length=32)  # Field name made lowercase.
    cpuspeed = models.CharField(db_column='CpuSpeed', max_length=32)  # Field name made lowercase.
    cpunum = models.IntegerField(db_column='CpuNum')  # Field name made lowercase.
    memorysize = models.IntegerField(db_column='MemorySize')  # Field name made lowercase.
    disksize = models.IntegerField(db_column='DiskSize')  # Field name made lowercase.
    lbip = models.CharField(db_column='LBIP', max_length=32)  # Field name made lowercase.
    serviceip = models.CharField(db_column='ServiceIP', max_length=32)  # Field name made lowercase.
    serverip = models.CharField(db_column='ServerIP', max_length=32)  # Field name made lowercase.
    usage = models.CharField(db_column='Usage', max_length=32)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=1024)  # Field name made lowercase.
    updatetime = models.DateField(db_column='UpdateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_appserver'


class CmVrmsWikiAppserverStoragedeviceid(models.Model):
    appserver = models.ForeignKey(CmVrmsWikiAppserver)
    storage_detail = models.ForeignKey('CmVrmsWikiStorageDetail')

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_appserver_storagedeviceid'
        unique_together = (('appserver_id', 'storage_detail_id'),)


class CmVrmsWikiCmApplication(models.Model):
    appid = models.AutoField(db_column='AppID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=64)  # Field name made lowercase.
    chinesename = models.CharField(db_column='ChineseName', max_length=128)  # Field name made lowercase.
    chineseabbreviation = models.CharField(db_column='ChineseAbbreviation', max_length=128)  # Field name made lowercase.
    englishname = models.CharField(db_column='EnglishName', max_length=64)  # Field name made lowercase.
    englishabbreviation = models.CharField(db_column='EnglishAbbreviation', max_length=32)  # Field name made lowercase.
    envtype = models.CharField(db_column='EnvType', max_length=32)  # Field name made lowercase.
    uatversion = models.CharField(db_column='UATVersion', max_length=32)  # Field name made lowercase.
    servicetype = models.CharField(db_column='ServiceType', max_length=64)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=64)  # Field name made lowercase.
    securitylevel = models.CharField(db_column='SecurityLevel', max_length=64)  # Field name made lowercase.
    launchdate = models.DateField(db_column='LaunchDate')  # Field name made lowercase.
    offdate = models.DateField(db_column='OffDate')  # Field name made lowercase.
    servicestart = models.TimeField(db_column='ServiceStart')  # Field name made lowercase.
    serviceend = models.TimeField(db_column='ServiceEnd')  # Field name made lowercase.
    duration = models.DecimalField(db_column='Duration', max_digits=10, decimal_places=5)  # Field name made lowercase.
    operationstart = models.TimeField(db_column='OperationStart')  # Field name made lowercase.
    operationend = models.TimeField(db_column='OperationEnd')  # Field name made lowercase.
    availabledate = models.CharField(db_column='AvailableDate', max_length=128)  # Field name made lowercase.
    uatrelease = models.CharField(db_column='UatRelease', max_length=300)  # Field name made lowercase.
    prodrelease = models.CharField(db_column='ProdRelease', max_length=300)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500)  # Field name made lowercase.
    updatedate = models.DateField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_cm_application'


class CmVrmsWikiCmApplicationMaintainer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    appid = models.ForeignKey(CmVrmsWikiCmApplication, db_column='AppID_id')  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=64)  # Field name made lowercase.
    cma = models.CharField(db_column='CMA', max_length=32)  # Field name made lowercase.
    cmb = models.CharField(db_column='CMB', max_length=32)  # Field name made lowercase.
    deilvera = models.CharField(db_column='DeilverA', max_length=32)  # Field name made lowercase.
    deilverb = models.CharField(db_column='DeilverB', max_length=32)  # Field name made lowercase.
    devpm = models.CharField(db_column='DevPM', max_length=32)  # Field name made lowercase.
    devcompany = models.CharField(db_column='DevCompany', max_length=64)  # Field name made lowercase.
    devcompanypm = models.CharField(db_column='DevCompanyPM', max_length=32)  # Field name made lowercase.
    testpm = models.CharField(db_column='TestPM', max_length=32)  # Field name made lowercase.
    testld = models.CharField(db_column='TestLD', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_cm_application_maintainer'


class CmVrmsWikiCmUsers(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    appserverid = models.ForeignKey(CmVrmsWikiAppserver, db_column='AppServerID_id')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=32)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=32)  # Field name made lowercase.
    expirationdate = models.DateField(db_column='ExpirationDate')  # Field name made lowercase.
    pgroupname = models.CharField(db_column='PGroupName', max_length=32)  # Field name made lowercase.
    sgroupname = models.CharField(db_column='SGroupName', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_cm_users'


class CmVrmsWikiConfigFile(models.Model):
    configid = models.AutoField(db_column='ConfigId', primary_key=True)  # Field name made lowercase.
    appserverid = models.ForeignKey(CmVrmsWikiAppserver, db_column='AppServerID_id')  # Field name made lowercase.
    configname = models.CharField(db_column='ConfigName', max_length=256)  # Field name made lowercase.
    userid = models.ForeignKey(CmVrmsWikiCmUsers, db_column='UserID_id')  # Field name made lowercase.
    configdescription = models.CharField(db_column='ConfigDescription', max_length=2048)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_config_file'


class CmVrmsWikiDb(models.Model):
    dbid = models.AutoField(db_column='DBID', primary_key=True)  # Field name made lowercase.
    softwareid = models.ForeignKey('CmVrmsWikiSoftware', db_column='SoftwareID_id')  # Field name made lowercase.
    instance_name = models.CharField(db_column='INSTANCE_NAME', max_length=32)  # Field name made lowercase.
    dbname = models.CharField(db_column='DBName', max_length=32)  # Field name made lowercase.
    datafile = models.CharField(db_column='DataFile', max_length=128)  # Field name made lowercase.
    logfile = models.CharField(db_column='LogFile', max_length=128)  # Field name made lowercase.
    port = models.CharField(db_column='Port', max_length=32)  # Field name made lowercase.
    dbuser = models.CharField(db_column='DbUser', max_length=32)  # Field name made lowercase.
    ha = models.CharField(db_column='HA', max_length=32)  # Field name made lowercase.
    member = models.CharField(db_column='MEMBER', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_db'


class CmVrmsWikiDevice(models.Model):
    deviceid = models.AutoField(db_column='DeviceID', primary_key=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='MANUFACTURER', max_length=64)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=64)  # Field name made lowercase.
    purchase_date = models.DateField(db_column='PURCHASE_DATE')  # Field name made lowercase.
    service_end_date = models.DateField(db_column='SERVICE_END_DATE')  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=32)  # Field name made lowercase.
    maintainera = models.CharField(db_column='maintainerA', max_length=32)  # Field name made lowercase.
    maintainerb = models.CharField(db_column='maintainerB', max_length=32)  # Field name made lowercase.
    district = models.CharField(db_column='DISTRICT', max_length=32)  # Field name made lowercase.
    room = models.CharField(db_column='ROOM', max_length=32)  # Field name made lowercase.
    cabinet = models.CharField(db_column='CABINET', max_length=32)  # Field name made lowercase.
    count_u = models.CharField(db_column='COUNT_U', max_length=32)  # Field name made lowercase.
    associatedeviceid = models.ForeignKey('self', db_column='AssociateDeviceid_id', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=1024)  # Field name made lowercase.
    updatetime = models.DateField(db_column='UpdateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_device'


class CmVrmsWikiEquipmentDetail(models.Model):
    equipmentid = models.AutoField(db_column='EquipmentId', primary_key=True)  # Field name made lowercase.
    deviceid = models.ForeignKey(CmVrmsWikiDevice, db_column='DeviceID_id')  # Field name made lowercase.
    devicesn = models.CharField(db_column='DeviceSN', max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1024)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_equipment_detail'


class CmVrmsWikiLb(models.Model):
    lbid = models.AutoField(db_column='LBID', primary_key=True)  # Field name made lowercase.
    appid = models.ForeignKey(CmVrmsWikiCmApplication, db_column='AppID_id')  # Field name made lowercase.
    lbname = models.CharField(db_column='LBName', max_length=64)  # Field name made lowercase.
    lbip = models.CharField(db_column='LBIP', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_lb'


class CmVrmsWikiLbMember(models.Model):
    lbid = models.ForeignKey(CmVrmsWikiLb, db_column='LBID_id')  # Field name made lowercase.
    appid = models.ForeignKey(CmVrmsWikiCmApplication, db_column='AppID_id')  # Field name made lowercase.
    appserverid = models.ForeignKey(CmVrmsWikiAppserver, db_column='AppServerID_id')  # Field name made lowercase.
    appserverip = models.CharField(db_column='AppServerIP', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_lb_member'


class CmVrmsWikiLicense(models.Model):
    licenseid = models.AutoField(db_column='LicenseID', primary_key=True)  # Field name made lowercase.
    appid = models.ForeignKey(CmVrmsWikiCmApplication, db_column='AppID_id')  # Field name made lowercase.
    appserverid = models.ForeignKey(CmVrmsWikiAppserver, db_column='AppServerID_id')  # Field name made lowercase.
    software = models.CharField(db_column='Software', max_length=256)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=32)  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=64)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_license'


class CmVrmsWikiLogFile(models.Model):
    logid = models.AutoField(db_column='LogId', primary_key=True)  # Field name made lowercase.
    appserverid = models.ForeignKey(CmVrmsWikiAppserver, db_column='AppServerID_id')  # Field name made lowercase.
    userid = models.ForeignKey(CmVrmsWikiCmUsers, db_column='UserID_id')  # Field name made lowercase.
    logpath = models.CharField(db_column='LogPath', max_length=256)  # Field name made lowercase.
    logdescription = models.CharField(db_column='LogDescription', max_length=256)  # Field name made lowercase.
    lifecycle = models.CharField(db_column='LifeCycle', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_log_file'


class CmVrmsWikiMount(models.Model):
    mountid = models.AutoField(db_column='MountID', primary_key=True)  # Field name made lowercase.
    storagedeviceid = models.ForeignKey('CmVrmsWikiStorageDetail', db_column='StorageDeviceId_id')  # Field name made lowercase.
    appserverid = models.ForeignKey(CmVrmsWikiAppserver, db_column='AppServerID_id')  # Field name made lowercase.
    mountpath = models.CharField(db_column='MountPath', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_mount'


class CmVrmsWikiMq(models.Model):
    mqid = models.AutoField(db_column='MQID', primary_key=True)  # Field name made lowercase.
    softwareid = models.ForeignKey('CmVrmsWikiSoftware', db_column='SoftwareID_id')  # Field name made lowercase.
    queuemanager = models.CharField(db_column='QueueManager', max_length=32)  # Field name made lowercase.
    qlocal = models.CharField(db_column='QLocal', max_length=32)  # Field name made lowercase.
    qremote = models.CharField(db_column='QRemote', max_length=32)  # Field name made lowercase.
    chanel = models.CharField(db_column='Chanel', max_length=32)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_mq'


class CmVrmsWikiNetdeviceDetail(models.Model):
    netdeviceid = models.AutoField(db_column='NetDeviceId', primary_key=True)  # Field name made lowercase.
    deviceid = models.ForeignKey(CmVrmsWikiDevice, db_column='DeviceID_id')  # Field name made lowercase.
    devicesn = models.CharField(db_column='DeviceSN', max_length=64)  # Field name made lowercase.
    netdevicetype = models.CharField(db_column='NetDeviceType', max_length=64)  # Field name made lowercase.
    manage_ip = models.CharField(db_column='MANAGE_IP', max_length=32)  # Field name made lowercase.
    ios_version = models.CharField(db_column='IOS_VERSION', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_netdevice_detail'


class CmVrmsWikiOther(models.Model):
    otherid = models.AutoField(db_column='OtherID', primary_key=True)  # Field name made lowercase.
    softwareid = models.ForeignKey('CmVrmsWikiSoftware', db_column='SoftwareID_id')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1024)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_other'


class CmVrmsWikiServerDetail(models.Model):
    serverid = models.AutoField(db_column='ServerId', primary_key=True)  # Field name made lowercase.
    deviceid = models.ForeignKey(CmVrmsWikiDevice, db_column='DeviceID_id')  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=64)  # Field name made lowercase.
    devicesn = models.CharField(db_column='DeviceSN', max_length=64)  # Field name made lowercase.
    server_type = models.CharField(db_column='Server_type', max_length=64)  # Field name made lowercase.
    cpu_type = models.CharField(db_column='CPU_TYPE', max_length=32)  # Field name made lowercase.
    cpu_frequency = models.CharField(db_column='CPU_FREQUENCY', max_length=32)  # Field name made lowercase.
    cpu_num = models.IntegerField(db_column='CPU_NUM')  # Field name made lowercase.
    cpu_core_num = models.IntegerField(db_column='CPU_CORE_NUM')  # Field name made lowercase.
    mem_type = models.CharField(db_column='MEM_TYPE', max_length=32)  # Field name made lowercase.
    mem_conf = models.CharField(db_column='MEM_CONF', max_length=1024)  # Field name made lowercase.
    mem_size = models.CharField(db_column='MEM_SIZE', max_length=32)  # Field name made lowercase.
    harddisk_capacity = models.CharField(db_column='HARDDISK_CAPACITY', max_length=1024)  # Field name made lowercase.
    disk_size = models.CharField(db_column='DISK_SIZE', max_length=32)  # Field name made lowercase.
    network_card = models.CharField(db_column='NETWORK_CARD', max_length=1024)  # Field name made lowercase.
    hbacard = models.CharField(db_column='HBACARD', max_length=1024)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_server_detail'


class CmVrmsWikiServerProcessPool(models.Model):
    processid = models.AutoField(db_column='ProcessId', primary_key=True)  # Field name made lowercase.
    appserverid = models.ForeignKey(CmVrmsWikiAppserver, db_column='AppServerID_id')  # Field name made lowercase.
    userid = models.ForeignKey(CmVrmsWikiCmUsers, db_column='UserID_id')  # Field name made lowercase.
    processname = models.CharField(db_column='ProcessName', max_length=64)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port')  # Field name made lowercase.
    function = models.CharField(db_column='Function', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_server_process_pool'


class CmVrmsWikiSoftware(models.Model):
    softwareid = models.AutoField(db_column='SoftwareID', primary_key=True)  # Field name made lowercase.
    appserverid = models.ForeignKey(CmVrmsWikiAppserver, db_column='AppServerID_id')  # Field name made lowercase.
    softwaretype = models.CharField(db_column='SoftwareType', max_length=24)  # Field name made lowercase.
    softwarename = models.CharField(db_column='SoftwareName', max_length=32)  # Field name made lowercase.
    installpath = models.CharField(db_column='InstallPath', max_length=256)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_software'


class CmVrmsWikiStorageDetail(models.Model):
    storageid = models.AutoField(db_column='StorageId', primary_key=True)  # Field name made lowercase.
    deviceid = models.ForeignKey(CmVrmsWikiDevice, db_column='DeviceID_id')  # Field name made lowercase.
    storage_name = models.CharField(db_column='STORAGE_NAME', max_length=32)  # Field name made lowercase.
    devicesn = models.CharField(db_column='DeviceSN', max_length=64)  # Field name made lowercase.
    firmware = models.CharField(db_column='Firmware', max_length=64)  # Field name made lowercase.
    ctlr_num = models.IntegerField(db_column='Ctlr_NUM')  # Field name made lowercase.
    disk_type = models.CharField(db_column='DISK_TYPE', max_length=32)  # Field name made lowercase.
    disk_capacity = models.CharField(db_column='DISK_Capacity', max_length=32)  # Field name made lowercase.
    disk_num = models.CharField(db_column='DISK_NUM', max_length=32)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=32)  # Field name made lowercase.
    expansibility = models.CharField(db_column='EXPANSIBILITY', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_storage_detail'


class CmVrmsWikiTomcat(models.Model):
    tomcatid = models.AutoField(db_column='TomcatID', primary_key=True)  # Field name made lowercase.
    softwareid = models.ForeignKey(CmVrmsWikiSoftware, db_column='SoftwareID_id')  # Field name made lowercase.
    port = models.IntegerField(db_column='Port')  # Field name made lowercase.
    sslport = models.IntegerField(db_column='SSLPort')  # Field name made lowercase.
    docmentroot = models.CharField(db_column='DocmentRoot', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_tomcat'


class CmVrmsWikiWeblogic(models.Model):
    weblogicid = models.AutoField(db_column='WeblogicID', primary_key=True)  # Field name made lowercase.
    softwareid = models.ForeignKey(CmVrmsWikiSoftware, db_column='SoftwareID_id')  # Field name made lowercase.
    consolecontexpath = models.CharField(db_column='ConsoleContexPath', max_length=128)  # Field name made lowercase.
    consoleusername = models.CharField(db_column='ConsoleUserName', max_length=24)  # Field name made lowercase.
    domianname = models.CharField(db_column='DomianName', max_length=32)  # Field name made lowercase.
    domainpath = models.CharField(db_column='DomainPath', max_length=128)  # Field name made lowercase.
    weblogicservername = models.CharField(db_column='WeblogicServerName', max_length=32)  # Field name made lowercase.
    listener = models.CharField(db_column='Listener', max_length=32)  # Field name made lowercase.
    ssllistener = models.CharField(db_column='SSLListener', max_length=32)  # Field name made lowercase.
    jdbctype = models.CharField(db_column='JDBCType', max_length=64)  # Field name made lowercase.
    jndiname = models.CharField(db_column='JNDIName', max_length=64)  # Field name made lowercase.
    jdbcurl = models.CharField(db_column='JDBCUrl', max_length=64)  # Field name made lowercase.
    driver = models.CharField(db_column='Driver', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_weblogic'


class CmVrmsWikiWeblogicApp(models.Model):
    appid = models.AutoField(db_column='AppID', primary_key=True)  # Field name made lowercase.
    serverid = models.ForeignKey('CmVrmsWikiWeblogicServer', db_column='ServerID_id')  # Field name made lowercase.
    appname = models.CharField(db_column='AppName', max_length=32)  # Field name made lowercase.
    deploypath = models.CharField(db_column='DeployPath', max_length=128)  # Field name made lowercase.
    deploytype = models.CharField(db_column='DeployType', max_length=32)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_weblogic_app'


class CmVrmsWikiWeblogicJdbc(models.Model):
    jdbcid = models.AutoField(db_column='JdbcID', primary_key=True)  # Field name made lowercase.
    weblogicid = models.ForeignKey(CmVrmsWikiWeblogic, db_column='WeblogicID_id')  # Field name made lowercase.
    jdbctype = models.CharField(db_column='JDBCType', max_length=64)  # Field name made lowercase.
    jndiname = models.CharField(db_column='JNDIName', max_length=64)  # Field name made lowercase.
    jdbcurl = models.CharField(db_column='JDBCUrl', max_length=64)  # Field name made lowercase.
    driver = models.CharField(db_column='Driver', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_weblogic_jdbc'


class CmVrmsWikiWeblogicJdbcMap(models.Model):
    serverid = models.ForeignKey('CmVrmsWikiWeblogicServer', db_column='ServerID_id')  # Field name made lowercase.
    jdbcid = models.ForeignKey(CmVrmsWikiWeblogicJdbc, db_column='JdbcID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_weblogic_jdbc_map'


class CmVrmsWikiWeblogicServer(models.Model):
    serverid = models.AutoField(db_column='ServerID', primary_key=True)  # Field name made lowercase.
    weblogicid = models.ForeignKey(CmVrmsWikiWeblogic, db_column='WeblogicID_id')  # Field name made lowercase.
    weblogicservername = models.CharField(db_column='WeblogicServerName', max_length=32)  # Field name made lowercase.
    listener = models.CharField(db_column='Listener', max_length=32)  # Field name made lowercase.
    ssllistener = models.CharField(db_column='SSLListener', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cm_vrms_wiki_weblogic_server'


class CqUatst(models.Model):
    severity = models.CharField(db_column='Severity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prjno = models.CharField(db_column='PrjNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unduplicate_state = models.CharField(max_length=255, blank=True, null=True)
    versionno = models.CharField(db_column='VersionNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbid = models.FloatField(blank=True, null=True)
    assign_date_old = models.DateTimeField(db_column='Assign_date_old', blank=True, null=True)  # Field name made lowercase.
    impatstart = models.DateTimeField(db_column='Impatstart', blank=True, null=True)  # Field name made lowercase.
    itil_id = models.CharField(db_column='ITIL_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    record_type = models.CharField(max_length=255, blank=True, null=True)
    impattime = models.CharField(db_column='ImpatTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prjname = models.CharField(db_column='PrjName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    submitdate = models.DateTimeField(db_column='Submitdate', blank=True, null=True)  # Field name made lowercase.
    testenv = models.CharField(db_column='TestEnv', max_length=255, blank=True, null=True)  # Field name made lowercase.
    check_flag = models.BigIntegerField(db_column='Check_flag', blank=True, null=True)  # Field name made lowercase.
    open_flag = models.BigIntegerField(db_column='Open_flag', blank=True, null=True)  # Field name made lowercase.
    defecttype = models.CharField(db_column='DefectType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    open_date_save = models.CharField(db_column='Open_date_save', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_duplicate = models.BigIntegerField(blank=True, null=True)
    open_date = models.DateTimeField(db_column='Open_date', blank=True, null=True)  # Field name made lowercase.
    validate_date_save = models.DateTimeField(db_column='Validate_date_save', blank=True, null=True)  # Field name made lowercase.
    planfinish = models.DateTimeField(db_column='Planfinish', blank=True, null=True)  # Field name made lowercase.
    date_flag = models.BigIntegerField(db_column='Date_flag', blank=True, null=True)  # Field name made lowercase.
    bugtype_1 = models.CharField(db_column='BugType_1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    assign_date = models.DateTimeField(db_column='Assign_date', blank=True, null=True)  # Field name made lowercase.
    is_active = models.BigIntegerField(blank=True, null=True)
    principal = models.CharField(db_column='Principal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    casystemname = models.CharField(db_column='CaSystemName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resolution = models.CharField(db_column='Resolution', max_length=255, blank=True, null=True)  # Field name made lowercase.
    actualfinish = models.DateTimeField(db_column='Actualfinish', blank=True, null=True)  # Field name made lowercase.
    close_date = models.DateTimeField(db_column='Close_date', blank=True, null=True)  # Field name made lowercase.
    version = models.BigIntegerField(blank=True, null=True)
    locked_by = models.BigIntegerField(blank=True, null=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    analysisresult = models.CharField(db_column='AnalysisResult', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impatend = models.DateTimeField(db_column='Impatend', blank=True, null=True)  # Field name made lowercase.
    submitter = models.CharField(db_column='Submitter', max_length=255, blank=True, null=True)  # Field name made lowercase.
    actualstart = models.DateTimeField(db_column='Actualstart', blank=True, null=True)  # Field name made lowercase.
    headline = models.CharField(db_column='Headline', max_length=255, blank=True, null=True)  # Field name made lowercase.
    validate_date = models.DateTimeField(db_column='Validate_date', blank=True, null=True)  # Field name made lowercase.
    rate = models.CharField(db_column='Rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resolve_date = models.DateTimeField(db_column='Resolve_date', blank=True, null=True)  # Field name made lowercase.
    resolve_date_save = models.CharField(db_column='Resolve_date_save', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bugtype_2 = models.CharField(db_column='BugType_2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resolve_time_save = models.DateTimeField(db_column='Resolve_time_save', blank=True, null=True)  # Field name made lowercase.
    impactnum = models.CharField(db_column='ImpactNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lock_version = models.BigIntegerField(blank=True, null=True)
    check_date = models.DateTimeField(db_column='Check_date', blank=True, null=True)  # Field name made lowercase.
    subsystemname = models.CharField(db_column='SubsystemName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    close_time_save = models.DateTimeField(db_column='Close_time_save', blank=True, null=True)  # Field name made lowercase.
    planstart = models.DateTimeField(db_column='Planstart', blank=True, null=True)  # Field name made lowercase.
    sumbit_date = models.DateTimeField(db_column='Sumbit_date', blank=True, null=True)  # Field name made lowercase.
    check_date_save = models.DateTimeField(db_column='Check_date_save', blank=True, null=True)  # Field name made lowercase.
    assign_date_save = models.DateTimeField(db_column='Assign_date_save', blank=True, null=True)  # Field name made lowercase.
    bugtype_3 = models.CharField(db_column='BugType_3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    open_time_save = models.DateTimeField(db_column='Open_time_save', blank=True, null=True)  # Field name made lowercase.
    owner_old = models.CharField(db_column='Owner_old', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cq_uatst'


class CustomFields(models.Model):
    id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    field_format = models.CharField(max_length=30)
    possible_values = models.CharField(max_length=5000, blank=True, null=True)
    regexp = models.CharField(max_length=255, blank=True, null=True)
    min_length = models.IntegerField(blank=True, null=True)
    max_length = models.IntegerField(blank=True, null=True)
    is_required = models.SmallIntegerField()
    is_for_all = models.SmallIntegerField()
    is_filter = models.SmallIntegerField()
    position = models.IntegerField(blank=True, null=True)
    searchable = models.SmallIntegerField(blank=True, null=True)
    default_value = models.TextField(blank=True, null=True)
    editable = models.SmallIntegerField(blank=True, null=True)
    visible = models.SmallIntegerField()
    multiple = models.SmallIntegerField(blank=True, null=True)
    format_store = models.CharField(max_length=5000, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_fields'


class CustomValues(models.Model):
    id = models.IntegerField(blank=True, null=True)
    customized_type = models.CharField(max_length=30)
    customized_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    value = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_values'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FileuploadPicture(models.Model):
    file = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'fileupload_picture'


class FileuploadSysconfinfo(models.Model):
    node_source = models.CharField(max_length=100)
    node_target = models.CharField(max_length=100)
    data_type = models.CharField(max_length=300)
    conn = models.CharField(max_length=300)
    conn_method = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'fileupload_sysconfinfo'


class FileuploadSysdatamineinfo(models.Model):
    node_source = models.CharField(max_length=100)
    node_target = models.CharField(max_length=100)
    data_type = models.CharField(max_length=300)
    conn = models.CharField(max_length=300)
    conn_method = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    from_info = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'fileupload_sysdatamineinfo'


class FileuploadSysteminfo(models.Model):

    class Meta:
        managed = False
        db_table = 'fileupload_systeminfo'


class FileuploadVerconfinfo(models.Model):
    main_up_sys_name = models.CharField(max_length=100)
    main_up_sys_version = models.CharField(max_length=100)
    main_up_sys_data_flow = models.CharField(max_length=30)
    relevant_sys_group = models.CharField(max_length=100)
    relevant_sys_name = models.CharField(max_length=100)
    relevant_sys_version = models.CharField(max_length=100)
    main_relevant_con_if_test = models.CharField(max_length=10)
    main_relevant_con_if_sync = models.CharField(max_length=10)
    depend_detail = models.CharField(max_length=1000)
    data_interaction_detail = models.CharField(max_length=1000)
    remark_col1 = models.CharField(max_length=200)
    remark_col2 = models.CharField(max_length=200)
    remark_col3 = models.CharField(max_length=200)
    remark_col4 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'fileupload_verconfinfo'


class FileuploadVersioninfo(models.Model):

    class Meta:
        managed = False
        db_table = 'fileupload_versioninfo'


class Issues(models.Model):
    id = models.IntegerField(blank=True, null=True)
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


class Projects(models.Model):
    id = models.IntegerField(blank=True, null=True)
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


class ReversionRevision(models.Model):
    manager_slug = models.CharField(max_length=191)
    date_created = models.DateTimeField()
    comment = models.TextField()
    user = models.ForeignKey(AuthUser, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reversion_revision'


class ReversionVersion(models.Model):
    object_id = models.TextField()
    object_id_int = models.IntegerField(blank=True, null=True)
    format = models.CharField(max_length=255)
    serialized_data = models.TextField()
    object_repr = models.TextField()
    content_type = models.ForeignKey(DjangoContentType)
    revision = models.ForeignKey(ReversionRevision)

    class Meta:
        managed = False
        db_table = 'reversion_version'


class TrackConnectWorkbooks(models.Model):
    workbook_name = models.CharField(max_length=30)
    sheet_name = models.CharField(max_length=30)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'track_connect_workbooks'


class Users(models.Model):
    id = models.IntegerField(blank=True, null=True)
    login = models.CharField(max_length=255)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'


class XadminBookmark(models.Model):
    title = models.CharField(max_length=128)
    user_id = models.IntegerField(blank=True, null=True)
    url_name = models.CharField(max_length=64)
    content_type_id = models.IntegerField()
    query = models.CharField(max_length=1000)
    is_share = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xadmin_bookmark'


class XadminUsersettings(models.Model):
    user_id = models.IntegerField()
    key = models.CharField(max_length=256)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'xadmin_usersettings'


class XadminUserwidget(models.Model):
    user_id = models.IntegerField()
    page_id = models.CharField(max_length=256)
    widget_type = models.CharField(max_length=50)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'xadmin_userwidget'
