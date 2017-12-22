# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0002_auto_20171107_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_img',
            field=models.ImageField(upload_to='', default=''),
        ),
    ]
