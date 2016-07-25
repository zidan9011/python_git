# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataExchangeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_num', models.CharField(max_length=500, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xbc\x96\xe5\x8f\xb7')),
                ('service_system', models.CharField(max_length=100, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\x8d\xe5\x8a\xa1\xe4\xbd\x93\xe7\xb3\xbb')),
                ('main_body', models.CharField(max_length=100, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xb8\xbb\xe9\xa2\x98\xe5\x9f\x9f')),
                ('data_entity', models.CharField(max_length=128, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x95\xb0\xe6\x8d\xae\xe5\xae\x9e\xe4\xbd\x93')),
                ('data_entity_type', models.CharField(max_length=128, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x95\xb0\xe6\x8d\xae\xe5\xae\x9e\xe4\xbd\x93\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('service_name', models.CharField(max_length=500, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x90\x8d\xe7\xa7\xb0')),
                ('mep', models.CharField(max_length=50, verbose_name=b'MEP(\xe6\xb6\x88\xe6\x81\xaf\xe4\xba\xa4\xe6\x8d\xa2\xe6\xa8\xa1\xe5\xbc\x8f)')),
                ('ispublic', models.CharField(max_length=50, verbose_name=b'\xe5\x85\xac\xe6\x9c\x89/\xe7\xa7\x81\xe6\x9c\x89')),
                ('other_interface_num', models.CharField(max_length=50, verbose_name=b'\xe5\xaf\xb9\xe6\x96\xb9\xe6\x8e\xa5\xe5\x8f\xa3\xe7\xbc\x96\xe5\x8f\xb7', blank=True)),
                ('interface_name', models.CharField(max_length=500, verbose_name=b'\xe6\x8e\xa5\xe5\x8f\xa3\xe5\x90\x8d\xe7\xa7\xb0')),
                ('interface_num', models.CharField(max_length=128, verbose_name=b'\xe6\x8e\xa5\xe5\x8f\xa3\xe7\xbc\x96\xe5\x8f\xb7')),
                ('merge_suggest', models.CharField(max_length=500, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x90\x88\xe5\xb9\xb6\xe5\xbb\xba\xe8\xae\xae')),
                ('update_time', models.CharField(max_length=500, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x95\xb0\xe6\x8d\xae\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('update_num', models.CharField(max_length=500, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x95\xb0\xe6\x8d\xae\xe6\x9b\xb4\xe6\x96\xb0\xe9\xa2\x91\xe7\x8e\x87', blank=True)),
                ('bi_service_number', models.CharField(max_length=500, verbose_name=b'\xe7\xa7\x81\xe6\x9c\x89\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x90\x8c\xe4\xb8\x80\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x8f\x8c\xe5\x90\x91\xe4\xba\xa4\xe4\xba\x92\xe7\xbc\x96\xe5\x8f\xb7', blank=True)),
                ('exchange_method', models.CharField(max_length=500, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae\xe4\xba\xa4\xe6\x8d\xa2\xe6\x96\xb9\xe5\xbc\x8f')),
                ('publisher', models.CharField(max_length=200, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x8f\x91\xe5\xb8\x83\xe8\x80\x85')),
                ('subscriber', models.CharField(max_length=200, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe8\xae\xa2\xe9\x98\x85\xe8\x80\x85')),
            ],
            options={
                'db_table': 'data_exchange',
                'verbose_name': '\u6570\u636e\u4ea4\u6362\u4fe1\u606f\u7ba1\u7406',
                'verbose_name_plural': '\u6570\u636e\u4ea4\u6362\u4fe1\u606f\u7ba1\u7406(\u603b)',
            },
        ),
        migrations.CreateModel(
            name='DataExInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='NameMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rawname', models.CharField(max_length=500, verbose_name=b'\xe5\x8e\x9f\xe5\xa7\x8b\xe5\x90\x8d')),
                ('mapname', models.CharField(max_length=500, verbose_name=b'\xe6\x98\xa0\xe5\xb0\x84\xe5\x90\x8d')),
            ],
            options={
                'db_table': 'namemap',
                'verbose_name': '\u7cfb\u7edf\u540d\u79f0\u6620\u5c04\u8868',
                'verbose_name_plural': '\u7cfb\u7edf\u540d\u79f0\u6620\u5c04\u8868(\u603b)',
            },
        ),
        migrations.CreateModel(
            name='NamemapInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(upload_to=b'pictures')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report_Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SystemName', models.CharField(max_length=128, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe5\x90\x8d\xe7\xa7\xb0')),
                ('VersionNum', models.CharField(max_length=16, verbose_name=b'\xe7\x89\x88\xe6\x9c\xac\xe5\x8f\xb7')),
                ('Main_SysName', models.CharField(max_length=128, verbose_name=b'\xe4\xb8\xbb\xe7\xb3\xbb\xe7\xbb\x9f\xe5\x90\x8d\xe7\xa7\xb0')),
                ('Main_VersionNum', models.CharField(max_length=16, verbose_name=b'\xe4\xb8\xbb\xe7\xb3\xbb\xe7\xbb\x9f\xe7\x89\x88\xe6\x9c\xac\xe5\x8f\xb7')),
                ('ProjectName', models.CharField(max_length=128, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('PlanTime', models.DateField(verbose_name=b'\xe7\x94\x9f\xe4\xba\xa7\xe4\xb8\x8a\xe7\xba\xbf\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('CRType', models.CharField(max_length=32, verbose_name=b'\xe5\x8f\x98\xe6\x9b\xb4\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'zc', b'\xe6\xad\xa3\xe5\xb8\xb8'), (b'jj', b'\xe7\xb4\xa7\xe6\x80\xa5'), (b'lx', b'\xe4\xbe\x8b\xe8\xa1\x8c'), (b'kj', b'\xe5\xbf\xab\xe6\x8d\xb7')])),
                ('TestType', models.CharField(max_length=32, verbose_name=b'\xe8\x81\x94\xe6\xb5\x8b\xe7\xb1\xbb\xe5\x88\xab', choices=[(b'zxt', b'\xe4\xb8\xbb\xe7\xb3\xbb\xe7\xbb\x9f'), (b'sjlc', b'\xe5\x8d\x87\xe7\xba\xa7\xe8\x81\x94\xe6\xb5\x8b'), (b'wyxlc', b'\xe6\x97\xa0\xe5\xbd\xb1\xe5\x93\x8d\xe8\x81\x94\xe6\xb5\x8b'), (b'whf', b'\xe6\x9c\xaa\xe5\x9b\x9e\xe5\xa4\x8d')])),
                ('ProjectStage', models.CharField(max_length=32, verbose_name=b'\xe7\x9b\xae\xe5\x89\x8d\xe9\xa1\xb9\xe7\x9b\xae\xe9\x98\xb6\xe6\xae\xb5', choices=[(b'cszb', b'\xe6\xb5\x8b\xe8\xaf\x95\xe5\x87\x86\xe5\xa4\x87'), (b'uat1cs', b'UAT1\xe6\xb5\x8b\xe8\xaf\x95'), (b'uat1wc', b'UAT1\xe5\xae\x8c\xe6\x88\x90'), (b'yslc', b'\xe9\xaa\x8c\xe6\x94\xb6\xe6\xb5\x81\xe7\xa8\x8b'), (b'yslc', b'\xe9\xaa\x8c\xe6\x94\xb6\xe6\xb5\x81\xe7\xa8\x8b'), (b'yscs', b'\xe9\xaa\x8c\xe6\x94\xb6\xe6\xb5\x8b\xe8\xaf\x95'), (b'mnlc', b'\xe6\xa8\xa1\xe6\x8b\x9f\xe6\xb5\x81\xe7\xa8\x8b'), (b'mncs', b'\xe6\xa8\xa1\xe6\x8b\x9f\xe6\xb5\x8b\xe8\xaf\x95'), (b'mnjd', b'\xe6\xa8\xa1\xe6\x8b\x9f\xe9\x98\xb6\xe6\xae\xb5'), (b'mnwc', b'\xe6\xa8\xa1\xe6\x8b\x9f\xe5\xae\x8c\xe6\x88\x90'), (b'ysx', b'\xe5\xb7\xb2\xe4\xb8\x8a\xe7\xba\xbf')])),
                ('TestRuns', models.CharField(blank=True, max_length=32, verbose_name=b'\xe6\xb5\x8b\xe8\xaf\x95\xe8\xbd\xae\xe6\xac\xa1', choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20')])),
                ('OverallSchedule', models.CharField(max_length=32, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x95\xb4\xe4\xbd\x93\xe8\xbf\x9b\xe5\xba\xa6', choices=[(b'zc', b'\xe6\xad\xa3\xe5\xb8\xb8'), (b'yq', b'\xe5\xbb\xb6\xe6\x9c\x9f'), (b'zt', b'\xe6\x9a\x82\xe5\x81\x9c'), (b'zf', b'\xe4\xbd\x9c\xe5\xba\x9f')])),
                ('Reason', models.CharField(max_length=2048, verbose_name=b'\xe5\x8e\x9f\xe5\x9b\xa0\xe8\xaf\xb4\xe6\x98\x8e', blank=True)),
                ('ManpowerInput', models.CharField(max_length=32, verbose_name=b'\xe4\xba\xba\xe5\x8a\x9b\xe6\x8a\x95\xe5\x85\xa5\xe6\x83\x85\xe5\x86\xb5', choices=[(b'rljz', b'\xe4\xba\xba\xe5\x8a\x9b\xe7\xb4\xa7\xe5\xbc\xa0'), (b'rlcz', b'\xe4\xba\xba\xe5\x8a\x9b\xe5\x85\x85\xe8\xb6\xb3'), (b'rlbz', b'\xe4\xba\xba\xe5\x8a\x9b\xe4\xb8\x8d\xe8\xb6\xb3')])),
                ('VersionQuality', models.CharField(max_length=32, verbose_name=b'\xe7\x89\x88\xe6\x9c\xac\xe8\xb4\xa8\xe9\x87\x8f', choices=[(b'zlyb', b'\xe8\xb4\xa8\xe9\x87\x8f\xe4\xb8\x80\xe8\x88\xac'), (b'zljh', b'\xe8\xb4\xa8\xe9\x87\x8f\xe8\xbe\x83\xe5\xa5\xbd'), (b'zljc', b'\xe8\xb4\xa8\xe9\x87\x8f\xe8\xbe\x83\xe5\xb7\xae')])),
                ('Workload', models.CharField(max_length=32, verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe9\x87\x8f\xe6\x83\x85\xe5\x86\xb5', choices=[(b'cqb', b'\xe8\xb6\x85\xe7\xad\xbe\xe6\x8a\xa5'), (b'zc', b'\xe6\xad\xa3\xe5\xb8\xb8'), (b'ccg', b'\xe8\xb6\x85\xe9\x87\x87\xe8\xb4\xad')])),
                ('PerformanceTest', models.CharField(blank=True, max_length=32, verbose_name=b'\xe6\x80\xa7\xe8\x83\xbd\xe6\xb5\x8b\xe8\xaf\x95', choices=[(b'y', b'\xe6\x9c\x89'), (b'n', b'\xe6\x97\xa0')])),
                ('Writter', models.CharField(max_length=32, verbose_name=b'\xe5\xa1\xab\xe5\x86\x99\xe4\xba\xba', blank=True)),
                ('UpdateDate', models.DateField(default=datetime.date(2016, 7, 6), verbose_name=b'\xe5\xa1\xab\xe5\x86\x99\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
            ],
            options={
                'db_table': 'test_report_Report_Detail',
                'verbose_name': '\u6d4b\u8bd5\u5468\u62a5\u4fe1\u606f',
                'verbose_name_plural': '\u6d4b\u8bd5\u5468\u62a5\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='Report_DetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='SysConfInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_source', models.CharField(max_length=100, verbose_name=b'\xe6\xba\x90\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('node_target', models.CharField(max_length=100, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('data_type', models.CharField(max_length=300, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('conn', models.CharField(max_length=300, verbose_name=b'\xe6\x8e\xa5\xe5\x8f\xa3')),
                ('conn_method', models.CharField(max_length=100, verbose_name=b'\xe6\x8e\xa5\xe5\x8f\xa3\xe6\x96\xb9\xe5\xbc\x8f')),
                ('type', models.CharField(max_length=100, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
            options={
                'db_table': 'fileupload_sysconfinfo',
                'verbose_name': '\u7cfb\u7edf\u4fe1\u606f\u7ba1\u7406',
                'verbose_name_plural': '\u7cfb\u7edf\u4fe1\u606f\u7ba1\u7406(\u603b)',
            },
        ),
        migrations.CreateModel(
            name='SysDataMineInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_source', models.CharField(max_length=100, verbose_name=b'\xe6\xba\x90\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('node_target', models.CharField(max_length=100, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('data_type', models.CharField(max_length=300, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('conn', models.CharField(max_length=300, verbose_name=b'\xe6\x8e\xa5\xe5\x8f\xa3')),
                ('conn_method', models.CharField(max_length=100, verbose_name=b'\xe6\x8e\xa5\xe5\x8f\xa3\xe6\x96\xb9\xe5\xbc\x8f')),
                ('type', models.CharField(max_length=100, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('from_info', models.CharField(max_length=500, verbose_name=b'\xe6\x8c\x96\xe6\x8e\x98\xe4\xbf\xa1\xe6\x81\xaf\xe6\x9d\xa5\xe6\xba\x90')),
            ],
            options={
                'db_table': 'fileupload_sysdatamineinfo',
                'verbose_name': '\u6316\u6398\u7cfb\u7edf\u4fe1\u606f\u7ba1\u7406',
                'verbose_name_plural': '\u6316\u6398\u7cfb\u7edf\u4fe1\u606f\u7ba1\u7406(\u603b)',
            },
        ),
        migrations.CreateModel(
            name='SysName_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SysName', models.CharField(max_length=256, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe5\x90\x8d\xe7\xa7\xb0')),
                ('map_sysname', models.CharField(max_length=256, verbose_name=b'\xe6\x98\xa0\xe5\xb0\x84\xe7\xb3\xbb\xe7\xbb\x9f\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'db_table': 'test_report_Sys_Name',
                'verbose_name': '\u6d4b\u8bd5\u5468\u62a5\u7cfb\u7edf\u540d\u79f0\u8868',
                'verbose_name_plural': '\u6d4b\u8bd5\u5468\u62a5\u7cfb\u7edf\u540d\u79f0\u8868',
            },
        ),
        migrations.CreateModel(
            name='SysNameInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='SystemInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='VerConfInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_up_sys_name', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\xbb\xe5\x8d\x87\xe7\xba\xa7\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('main_up_sys_version', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\xbb\xe5\x8d\x87\xe7\xba\xa7\xe7\x89\x88\xe6\x9c\xac')),
                ('main_up_sys_data_flow', models.CharField(blank=True, max_length=30, verbose_name=b'\xe6\x96\xb0\xe5\xa2\x9e\xe6\x95\xb0\xe6\x8d\xae\xe6\xb5\x81\xe5\x90\x91', choices=[(b'->', b'->'), (b'<-', b'<-'), (b'<->', b'<->')])),
                ('relevant_sys_group', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x9b\xae\xe6\xa0\x87\xe7\xbe\xa4', choices=[(b'hx', b'\xe6\xa0\xb8\xe5\xbf\x83\xe4\xba\xa4\xe6\x98\x93\xe5\xb9\xb3\xe5\x8f\xb0'), (b'yh', b'\xe7\x94\xa8\xe6\x88\xb7\xe6\x8e\xa5\xe5\x85\xa5\xe5\xb9\xb3\xe5\x8f\xb0'), (b'gg', b'\xe5\x85\xac\xe5\x85\xb1\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xb9\xb3\xe5\x8f\xb0'), (b'xx', b'\xe4\xbf\xa1\xe6\x81\xaf\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xb9\xb3\xe5\x8f\xb0'), (b'sj', b'\xe6\x95\xb0\xe6\x8d\xae\xe4\xba\xa4\xe6\x8d\xa2\xe5\xb9\xb3\xe5\x8f\xb0'), (b'jyh', b'\xe4\xba\xa4\xe6\x98\x93\xe5\x90\x8e\xe5\xa4\x84\xe7\x90\x86\xe5\xb9\xb3\xe5\x8f\xb0'), (b'bg', b'\xe5\x8a\x9e\xe5\x85\xac\xe6\x94\xaf\xe6\x8c\x81\xe5\xb9\xb3\xe5\x8f\xb0'), (b'yw', b'\xe8\xbf\x90\xe7\xbb\xb4\xe5\xb9\xb3\xe5\x8f\xb0'), (b'dsf', b'\xe7\xac\xac\xe4\xb8\x89\xe6\x96\xb9\xe6\x89\x98\xe7\xae\xa1\xe5\xb9\xb3\xe5\x8f\xb0'), (b'zz', b'Comstar\xe5\xa2\x9e\xe5\x80\xbc\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xb9\xb3\xe5\x8f\xb0')])),
                ('relevant_sys_name', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('relevant_sys_version', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\xb3\xbb\xe7\xbb\x9f\xe7\x89\x88\xe6\x9c\xac', blank=True)),
                ('main_relevant_con_if_test', models.CharField(max_length=10, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\x81\x94\xe6\xb5\x8b', choices=[(b'Y', b'Y'), (b'N', b'N')])),
                ('main_relevant_con_if_sync', models.CharField(max_length=10, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x90\x8c\xe6\xad\xa5\xe5\x8d\x87\xe7\xba\xa7', choices=[(b'Y', b'Y'), (b'N', b'N')])),
                ('depend_detail', models.CharField(max_length=1000, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae\xe4\xbe\x9d\xe8\xb5\x96\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('data_interaction_detail', models.CharField(max_length=1000, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae\xe4\xba\xa4\xe4\xba\x92\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('remark_col1', models.CharField(max_length=200, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xb7\xb2\xe4\xbf\xae\xe6\x94\xb9', blank=True)),
                ('remark_col2', models.CharField(max_length=200, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa82', blank=True)),
                ('remark_col3', models.CharField(max_length=200, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa83', blank=True)),
                ('remark_col4', models.CharField(max_length=200, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa84', blank=True)),
            ],
            options={
                'db_table': 'fileupload_verconfinfo',
                'verbose_name': '\u7248\u672c\u4fe1\u606f\u7ba1\u7406',
                'verbose_name_plural': '\u7248\u672c\u4fe1\u606f\u7ba1\u7406(\u603b)',
            },
        ),
        migrations.CreateModel(
            name='VersionInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
    ]
