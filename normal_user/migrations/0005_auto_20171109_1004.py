# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0004_auto_20171108_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pro_img',
            field=models.ImageField(default=None, verbose_name='产品图片', upload_to=''),
        ),
        migrations.AddField(
            model_name='products',
            name='pro_num',
            field=models.CharField(default=0, verbose_name='产品编号', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='pro_type',
            field=models.CharField(default=None, verbose_name='产品类型', max_length=30),
            preserve_default=False,
        ),
    ]
