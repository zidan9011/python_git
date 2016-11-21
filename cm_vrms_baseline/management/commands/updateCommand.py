#-*-coding:utf-8-*-

from django.core.management.base import BaseCommand
from cm_vrms_baseline.views import update_db_data
import time

class Command(BaseCommand):
	def handle(self, *args, **options):
		'''执行数据库更新任务'''
		update_db_data()
		with open('updateCommand.log','a+') as f:
			f.write('timer function called at ---> ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '.\n')
