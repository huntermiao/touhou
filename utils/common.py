# -*-coding:utf-8 -*-

#对需要的一些功能进行封装

import hashlib
from .wrappers import *
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from normal_user.models import *
import os
import time
import re
import shutil
# 密码加密
def password_encryption(password):

    # 创建加密对象
    sha = hashlib.sha256()
    # 对明文加密
    new_password = 'helloworld' + password
    sha.update(new_password.encode('utf-8'))
    # 返回密文
    return sha.hexdigest()

#CheckSum 加密

def CheckSum_en(str):
    sha = hashlib.sha1()
    sha.update(str.encode('utf-8'))
    return  sha.hexdigest()
# 用户是否登录
def login_permission(view_func):

    def wrapper(request, *args, **kwargs):
        # 检查用户是否登录
        if get_session(request, 'user_name') and get_session(request, 'user_id'):
            # 如果登录则执行视图函数
            #获取登录信息

            return view_func(request, *args, **kwargs)
        else:
            # 如果没有登录,跳转到登录页面
            return redirect(reverse('users:login'))

    return wrapper


#用户是否登录后进入登录页
def is_login(view_func):

    def wrapper(request, *args, **kwargs):
        # 检查用户是否登录
        if get_session(request, 'user_name') and get_session(request, 'user_id'):
            # 如果登录则执行视图函数
            return redirect(reverse('users:index'))
        else:
            # 如果没有登录,跳转到登录页面
            return view_func(request, *args, **kwargs)

    return wrapper

#创建保存图片目录
def makeNowdir(src):
    old_src = re.match('/(static/upload/(.*))',src).group(1)
    img_src = re.match('/(static/upload/(.*))', src).group(2)
    localstime = time.localtime(time.time())
    #设置根目录
    g_src= 'static/up_img/'
    new_src = g_src+str(localstime[0])+'/'+str(localstime[1])
    #判断目录是否存在
    if os.path.exists(g_src+'/'+str(localstime[0])):
        if os.path.exists(new_src):
            move_img(old_src,new_src)
        else:
            os.makedirs(new_src)
            move_img(old_src, new_src)
    else:
        os.makedirs(new_src)
        move_img(old_src, new_src)
    return new_src
#转移图片
def move_img(src,new_src):
    try:
        shutil.move(src,new_src)
    except Exception as e:
        return new_src



