# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0005_auto_20171109_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pro_units',
            field=models.CharField(verbose_name='产品单位', max_length=10, default='/个'),
        ),
    ]
