# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm_vrms_wiki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageStore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, null=True)),
                ('img', models.ImageField(upload_to=b'img')),
                ('AppServerID', models.ForeignKey(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\xbc\x96\xe5\x8f\xb7', to='cm_vrms_wiki.Appserver')),
            ],
            options={
                'db_table': 'cm_vrms_wiki_image_store',
                'verbose_name': '\u670d\u52a1\u5668\u67b6\u6784\u56fe',
                'verbose_name_plural': '\u670d\u52a1\u5668\u67b6\u6784\u56fe\u8868',
            },
        ),
    ]
