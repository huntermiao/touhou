# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0006_products_pro_units'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('creat_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('pro_name', models.CharField(max_length=20)),
                ('pro_css', models.CharField(max_length=20)),
                ('pro_image', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('creat_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('img_url', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='products',
            name='pro_sale',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_type',
            field=models.ForeignKey(to='normal_user.ProductsCategory'),
        ),
        migrations.AddField(
            model_name='productsimages',
            name='img_goods',
            field=models.ForeignKey(to='normal_user.Products'),
        ),
    ]
