# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0008_auto_20171109_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('creat_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('con_year', models.CharField(verbose_name='创建年份', max_length=4)),
                ('con_month', models.CharField(verbose_name='创建月份', max_length=2)),
                ('con_day', models.CharField(verbose_name='创建日期', max_length=2)),
                ('con_nums', models.IntegerField()),
                ('con_pro', models.ForeignKey(to='normal_user.Products')),
                ('con_user', models.ForeignKey(to='normal_user.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
