# -*-coding:utf-8 -*-

from utils.wrappers import *
import re
from .models import *
from django.contrib import messages
from utils.wrappers import *
from utils.common import *
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.conf import settings
from django.core.mail import send_mail
from itertools import islice
import csv
import random
def check_register_params(request):

    # 获得表单数据
    user_name = post(request, 'user_name')
    user_pass1 = post(request, 'pass_word')
    user_phone = post(request, 'phone_num')

    flag = True

    if not (5 <= len(user_name) <= 20):
        flag = False
        # 存储错误信息
        # request对象  信息类别messages.INFO 要显示的信息
        # messages.add_message(request, messages.INFO, '您输入的用户名长度不合法!')
        add_info_message(request, 'user_name', '请填写正确的姓名!')

    if not (8 <= len(user_pass1) <= 20):
        flag = False
        # messages.add_message(request, messages.INFO, '您输入的密码长度不合法!')
        add_info_message(request, 'user_pass', '密码格式错误!')

    if not (len(user_phone) == 11):
        flag = False
        # messages.add_message(request, messages.INFO, '您输入的密码长度不合法!')
        add_info_message(request, 'user_phone', '手机号码错误!')

    if Staff.objects.get_userinfo_by_name(user_name):
        flag = False
        # messages.add_message(request, messages.INFO, '用户名已经存在!')
        add_info_message(request, 'user_name', '用户名已经存在!')

    return flag



# 检测用户登录
def check_login_params(request):

    # 获得登录表单的用户名和密码
    user_name = post(request, 'login_user_name')
    user_pass = post(request, 'login_pass_word')
    # 判断用户名和密码的长度是否合法
    if not (5 <= len(user_name) <= 20):
        add_info_message(request, 'login_user_name', '用户名错误!')
        return False

    if not (8 <= len(user_pass) <= 20):
        add_info_message(request, 'login_user_pass', '密码错误!')
        return False

    # 查询用户名对应用户信息是否存在
    staff = Staff.objects.get_userinfo_by_name(user_name)
    if not staff:
        add_info_message(request, 'login_user_name', '用户不存在!')
        return False

    # 检查用户输入的密码是否正确
    if staff.staff_pass != password_encryption(user_pass):
        add_info_message(request, 'login_user_pass', '密码错误,请查证后再输入!')
        return False

    return True


# 保持用户登录状态
def keep_user_online(request):

    # 获得用户名
    user_name = post(request, 'login_user_name')
    # 获得用户id
    user = Staff.objects.get_userinfo_by_name(user_name)
    user_id = user.id
    # 保存用户名和id
    set_session(request, 'user_name', user_name)
    set_session(request, 'user_id', user_id)


# 记住用户名
def remember_username(request, response):

    # 记住用户名
    user_name = post(request, 'login_user_name')
    set_cookie(response, 'user_name', user_name)


# 用户联系方式信息校验
def check_update_address_params(request):

    # 获得表单数据
    user_recv = post(request, 'user_recv')
    user_addr = post(request, 'user_addr')
    user_code = post(request, 'user_code')
    user_tele = post(request, 'user_tele')

    if len(user_recv) == 0:
        return False

    if len(user_addr) == 0:
        return False

    if len(user_code) != 6:
        return False

    if len(user_tele) != 11:
        return False

    return True


# 生成激活链接
def create_active_link(request):

    serializer = Serializer(settings.SECRET_KEY, 3600)
    # 查询注册用户的ID
    user = User.objects.get_userinfo_by_name(post(request, 'user_name'))
    # 生成激活token
    token = serializer.dumps({'id': user.id})
    # 创建激活链接: http://localhost:8000/users/active_handle/asdasdadas345345/
    url = 'http://localhost:8000/users/active_handle/' + token.decode() + '/'

    return url


# 发送激活邮件
def send_active_mail(request):

    # 获得注册信息
    user_name = post(request, 'user_name')
    user_mail = post(request, 'user_mail')

    # 生成注册激活链接
    active_url = create_active_link(request)

    html_content = '尊敬的%s，欢迎您注册天天生鲜!<br>请点击链接完成激活:<br>激活地址:%s' % (user_name, active_url)

    send_mail(subject='天天生鲜注册激活邮件',
              message='', from_email=settings.EMAIL_HOST_USER,
              html_message=html_content,
              recipient_list=[user_mail])

#通过搜索进行模糊查询用户
def search_get(request):
    search_key = post(request,'search_key')
    if not search_key:
        return None
    #如果名字中包含search_key
    # todo 将链接的数据库分离
    if User.objects.filter(user_name__contains = search_key):
        user_list = User.objects.filter(user_name__contains = search_key)
        return  user_list
    # 如果编号号=search_key
    if User.objects.filter(user_num = search_key):
        user_list = User.objects.filter(user_num = search_key)
        return  user_list
    # 如果手机号=search_key
    if User.objects.filter(user_phone = search_key):
        user_list = User.objects.filter(user_phone = search_key)
        return  user_list
    return None


#字典化获取到的对象
def dumps(list):
    #新建空列表
    lists= []
    for lis in list:
        # 新建空字典
        dicts = {}
        dicts['user_name'] = lis.user_name
        dicts['user_num'] = lis.user_num
        dicts['user_phone'] = lis.user_phone
        dicts['user_birth'] = lis.user_birth
        dicts['user_address'] = lis.user_address
        dicts['user_age'] = lis.user_age
        lists.append(dicts)
    return  lists

#字典化上传的对象
def dumps_csv(src):
    csv_reader = csv.reader(open(src, encoding='utf-8'))
    lists= []
    for row in islice(csv_reader, 1, None):
        dicts = {}
        dicts['user_name'] = row[0]
        dicts['user_num'] = row[1]
        dicts['user_phone'] = row[2]
        dicts['user_birth'] = row[3]
        dicts['user_address'] = row[4]
        dicts['user_age'] = row[5]
        #去重
        if dicts in lists:
            continue
        #去空
        if not dicts['user_name']:
            continue
        lists.append(dicts)

    return  lists

def dumps_csv3(src):
    try:
        csv_reader = csv.reader(open(src, encoding='utf-8'))
        lists= []
        for row in islice(csv_reader, 1, None):
            if len(row) >3:
                return None
            dicts = {}
            dicts['pro_num'] = row[2]
            dicts['pro_name'] = row[1]
            dicts['sale_num'] = row[0]
            #去重
            if dicts in lists:
                continue
            #去空
            if not dicts['pro_num']:
                continue
            lists.append(dicts)
        return  lists
    except Exception as e:
        return None
#字典化上传的对象
#todo 将这两个方法合并
def dumps_csv2(src):
    try:
        csv_reader = csv.reader(open(src, encoding='utf-8'))
        lists= []
        for row in islice(csv_reader, 1, None):
            dicts = {}
            dicts['pro_img'] = row[0]
            dicts['pro_name'] = row[1]
            dicts['pro_num'] = row[2]
            dicts['pro_price'] = row[3]
            dicts['sto_stock'] = row[4]
            dicts['pro_units'] = row[5]
            dicts['pro_short'] = row[6]
            #去重
            if dicts in lists:
                continue
            #去空
            if not dicts['pro_img']:
                continue
            lists.append(dicts)
    except:
        lists = None
    return  lists

#判断上传的用户编号是否存在
def is_exist(name):
    if User.objects.filter(user_num=name):
        return False
    else:
        return True


def save_csvs(data):
    #获取所有保存的user对象
    #遍历字典对象
    flag = False
    for dic in data:
        # 创建用来保存的user对象

        if is_exist(dic['user_num']):
            flag = True
            user = User()
            print(user)
            user.user_name = dic['user_name']
            user.user_num = dic['user_num']
            user.user_phone = dic['user_phone']
            user.user_birth = dic['user_birth']
            user.user_address = dic['user_address']
            user.user_age = dic['user_age']

            user.save()
    return flag

#通过搜索进行模糊查询用户
def pro_search_get(request):
    search_key = post(request,'search_key')
    if not search_key:
        return None
    #如果名字中包含search_key
    # todo 将链接的数据库分离
    flag = True
    if Products.objects.filter(pro_name__contains = search_key):

        Products_list = Products.objects.filter(pro_name__contains = search_key)
        flag=False
        return  Products_list
    # 如果编号号=search_key
    if Products.objects.filter(pro_num = search_key):
        Products_list = Products.objects.filter(pro_num = search_key)
        flag = False
        return  Products_list

    return None

#字典化获取到的对象
def pro_dumps(list):
    #新建空列表
    lists= []
    for lis in list:
        # 新建空字典

        dicts = {}
        dicts['pro_name'] = lis.pro_name
        dicts['pro_price'] = lis.pro_price
        dicts['pro_num'] = lis.pro_num
        dicts['pro_short'] = lis.pro_short
        dicts['pro_img'] = str(lis.pro_img)
        try:
            dicts['sto_stock'] = lis.storage_set.order_by('-id').filter(is_delete=False)[0].sto_stock
        except Exception as e:
            print(e)
        dicts['pro_units'] = lis.pro_units
        dicts['pro_id'] = lis.id
        lists.append(dicts)
    return  lists

def check_pro(data):
    if Products.objects.filter(pro_num=data['pro_num']):
        return False
    else:
        return True
def save_sto(data,pid):
    sto = Storage()
    sto.sto_stock = data['pro_stock']
    sto.sto_pro_id = pid
    sto.save()
def save_pro(data):
    pro = Products()
    pro.pro_name=data['pro_name']
    pro.pro_price=data['pro_price']
    pro.pro_units=data['pro_units']
    pro.pro_num = data['pro_num']
    pro.pro_img=data['pro_img']
    pro.pro_short=data['pro_short']
    pro.pro_desc=data['pro_desc']
    pro.pro_type_id = 1
    pro.save()
    save_sto(data,pro.id)

def load_bulk(file_name,start,limit):
    src = 'static/upload/'+file_name
    try:
        starts= int(start)+1
        limits= int(limit)
        csv_reader = csv.reader(open(src, encoding='utf-8'))
        csv_list = list(csv_reader)
        lens= len(csv_list)
        if (starts+limits) <= lens:
            data = csv_list[starts:starts+limits]
            return data
        elif lens < starts:
            print('超限')
        elif starts < lens ==(starts+limits):
            data = csv_list[starts:starts + limits]
            return data
        elif starts<= lens <(starts+limits):
            data = csv_list[starts:lens]
            return data
    except Exception as e:
        print(e)

def dumps_list(list):
    lists = []
    for row in list:
        dicts = {}
        dicts['pro_img'] = row[0]
        dicts['pro_name'] = row[1]
        dicts['pro_num'] = row[2]
        dicts['pro_price'] = row[3]
        dicts['sto_stock'] = row[4]
        dicts['pro_units'] = row[5]
        dicts['pro_short'] = row[6]
        lists.append(dicts)

    return lists

#判断是否已经有此产品如果存在就返回False
def check_pro_list(num):
    try:
        if Products.objects.filter(pro_num=num):
            return False
        else:
            return True
    except Exception as e:
        print(e)


def bulk_save_sto(data,pid):
    sto = Storage()
    sto.sto_stock = data
    sto.sto_pro_id = pid
    sto.save()
def bulk_save_sql(file_name):
    flag = True
    src='static/upload/'+file_name
    img_src='static/bulk_img/'
    csv_reader = csv.reader(open(src, encoding='utf-8'))
    for row in islice(csv_reader, 1, None):
        pro_num = row[2]
        if check_pro_list(pro_num):
            pro = Products()
            pro.pro_name = row[1]
            pro.pro_price = row[3]
            pro.pro_units = row[5]
            pro.pro_num = row[2]
            pro.pro_img = img_src+row[0]+'.jpg'
            pro.pro_short = row[6]
            pro.pro_type_id = 1
            pro.save()
            bulk_save_sto(row[4], pro.id)
        else:
            flag = False

    return flag

#存储新的库存数据
def sale_save(pid,out):
    try:
        last_stock = Storage.objects.filter(sto_pro_id=pid).last().sto_stock
        sto = Storage()
        sto.sto_out = out
        sto.sto_into = 0
        sto.sto_stock = int(last_stock)-int(out)
        sto.sto_pro_id = pid
        sto.save()
        return  sto.sto_stock
    except Exception as e:
        print(e)
        return False


def bulk_sale_save_fu(data):
    flag = True
    for row in data:
        try:
            pro = Products.objects.filter(pro_num=row['pro_num'])
            print(pro.first().id)
            sale_save(pro.first().id, row['sale_num'])
        except Exception as e:
            flag=False
    return flag

# 查询数据
def search_for_key(key):
    stock = Storage.objects.filter(is_delete=False)
    list_num=[]
    list_lists=[]
    for i in stock:
        if re.match(key, str(i.sto_time)):
            if (i.sto_out > 0):
                pro = Products.objects.filter(id=i.sto_pro_id).last()
                if pro.pro_num in list_num:
                    dists_index = list_num.index(pro.pro_num)
                    list_lists[dists_index]['out'] = list_lists[dists_index]['out'] + i.sto_out
                else:
                    dists = {}
                    dists['name'] = pro.pro_name
                    dists['out'] = i.sto_out
                    dists['pid'] = pro.pro_num
                    dists['pro_img'] = pro.pro_img
                    list_num.append(pro.pro_num)
                    list_lists.append(dists)
    # lambda函数
    list_lists = sorted(list_lists, key=lambda x: x['out'], reverse=True)
    return list_lists
# 查看当年总销售额
def search_sale(data_dis):
    now_year = time.localtime(time.time())[0]
    now_month = time.localtime(time.time())[1]
    now_day = time.localtime(time.time())[2]
    if data_dis['year'] =='请选择年份' or data_dis['year'] =='':
        ruler = str(now_year) + '-' + str(now_month) + '-' + str(now_day)
    elif data_dis['mother'] =='请选择月份' or data_dis['mother'] =='':
        now_year = data_dis['year']
        ruler = str(now_year) + '.*'
    elif data_dis['day'] == '请选择日期' or data_dis['day'] == '':
        now_year = data_dis['year']
        now_month = data_dis['mother']
        ruler = str(now_year) + '-' + str(now_month) + '.*'
    else:
        now_year = data_dis['year']
        now_month = data_dis['mother']
        now_day = data_dis['day']
        ruler = str(now_year) + '-' + str(now_month) + '-' + str(now_day)
        # if types in type_list:
        #     if types == 'year':
        #         ruler =str(now_year)+'.*'
        #     elif types =='month':
        #         ruler = str(now_year) +'-'+ str(now_month)+'.*'
        #     else:
        #         ruler = str(now_year) +'-'+ str(now_month) +'-'+ str(now_day)
        #     print(ruler)
    list_lists = search_for_key(ruler)
    return list_lists

def createPhoneCode(session):
  chars=['0','1','2','3','4','5','6','7','8','9']
  x = random.choice(chars),random.choice(chars),random.choice(chars),random.choice(chars)
  verifyCode = "".join(x)
  session["phoneVerifyCode"] = {"time":int(time.time()), "code":verifyCode}
  return verifyCode