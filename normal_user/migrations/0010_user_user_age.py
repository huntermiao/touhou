# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0009_consumption'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_age',
            field=models.CharField(default='保密', max_length=3, verbose_name='会员年龄'),
        ),
    ]
