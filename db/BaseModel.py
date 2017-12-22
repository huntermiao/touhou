# -*-coding:utf-8 -*-
from django.db import models

class BaseModels(models.Model):
    creat_time = models.DateField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateField(auto_now=True,verbose_name='创建时间')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    class Meta:

        #设置这个类文件为基类
        abstract = True