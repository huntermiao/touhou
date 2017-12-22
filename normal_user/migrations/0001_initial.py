# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cources',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('creat_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('cource_name', models.CharField(verbose_name='服务名称', max_length=20)),
                ('cource_price', models.IntegerField(verbose_name='服务价格', default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('creat_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('pro_name', models.CharField(verbose_name='产品名称', max_length=20)),
                ('pro_price', models.IntegerField(verbose_name='产品价格', default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('creat_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('staff_name', models.CharField(verbose_name='员工姓名', max_length=20)),
                ('staff_num', models.CharField(null=True, verbose_name='员工编号', max_length=20)),
                ('staff_pass', models.CharField(verbose_name='员工密码', max_length=40)),
                ('staff_phone', models.CharField(null=True, verbose_name='员工手机', max_length=11)),
                ('staff_address', models.CharField(verbose_name='员工住址', max_length=255)),
                ('staff_permissions', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('creat_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('sto_time', models.DateField(auto_now_add=True, verbose_name='修改时间')),
                ('sto_stock', models.IntegerField(verbose_name='库存', default=0)),
                ('sto_out', models.IntegerField(verbose_name='出库', default=0)),
                ('sto_into', models.IntegerField(verbose_name='入库', default=0)),
                ('sto_pro', models.ForeignKey(verbose_name='产品id', to='normal_user.Products')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('creat_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('user_name', models.CharField(verbose_name='用户名', max_length=20)),
                ('user_num', models.CharField(null=True, verbose_name='会员号', max_length=20)),
                ('user_pass', models.CharField(verbose_name='用户密码', max_length=40)),
                ('user_marriage', models.CharField(verbose_name='婚姻状况', default='未知', max_length=6)),
                ('user_phone', models.CharField(null=True, verbose_name='用户手机', max_length=11)),
                ('user_birth', models.CharField(verbose_name='用户生日', max_length=20)),
                ('user_address', models.CharField(verbose_name='用户地址', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
