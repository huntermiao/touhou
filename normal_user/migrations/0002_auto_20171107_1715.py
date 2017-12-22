# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_pass',
            field=models.CharField(verbose_name='员工密码', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_pass',
            field=models.CharField(verbose_name='用户密码', max_length=64),
        ),
    ]
