# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0003_staff_staff_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_img',
            field=models.ImageField(upload_to='', default=None),
        ),
    ]
