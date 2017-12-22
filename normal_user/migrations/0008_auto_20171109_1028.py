# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0007_auto_20171109_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pro_desc',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='pro_short',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
    ]
