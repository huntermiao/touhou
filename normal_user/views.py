from django.shortcuts import render
from django.http import HttpResponse
from  django.shortcuts import redirect
from django.core.urlresolvers import reverse
from  .function import *
from  .models import *
#引入json
from  django.http import JsonResponse
#引入分页
from django.core.paginator import Paginator
# Create your views here.
from django.core.cache import cache
import csv
import json
import os
import requests


@is_login
def login(request):
    #显示login页面
    message = get_info_messages(request)
    try:
        # 判断是不是登出过
        isActive = message['isActive']
    except:
        isActive = '0'
    return render(request,'users/login.html',locals())



def register_handle(request):
    #注册
    if check_register_params(request):
        #保存注册信息
        Staff.objects.register_userinfo_save(request)
        #注册成功返回200
        return JsonResponse({'code':200})
    else:
        #注册失败返回300
        message = get_info_messages(request)
        return JsonResponse({'code':300,'message':message})

def login_handle(request):
    #登录
    if check_login_params(request):
        #保持用户登录状态
        keep_user_online(request)
        #设置要跳转的目标
        response = redirect(reverse('users:index'))
        #记住用户名
        remember_username(request, response)
        return response
    else:
        return redirect(reverse('users:login'))

# 用户登出
def logout(request):
    # 1. 清除用户session
    del_session(request)
    # 2.写下登录状态
    add_info_message(request, 'isActive', '1')
    # 3. 跳转到登录页面
    return redirect(reverse('users:login'))

@login_permission
def index(request):
    staff = get_user_login(request,Staff)
    #显示login页面
    return render(request,'users/index.html',locals())
@login_permission
def table(request):
    return render(request,'users/sales_table.html',locals())
@login_permission
def table(request):
    #传递登录信息
    staff = get_user_login(request, Staff)
    #读取用户列表
    # todo 将链接的数据库分离
    user_list = User.objects.filter(is_delete=False)
    #创建分页对象
    paginator =  Paginator(user_list,10)
    #获得当前的页码
    page = get(request, 'page')
    if not page:
        page = 1
    # 获得当前页码数据
    current_data = paginator.page(page)
    print(paginator.page_range)
    return render(request,'users/table.html',locals())

@login_permission
def datatable(request):
    staff = get_user_login(request, Staff)
    #获取user表的所有数据

    return render(request, 'users/datatable.html', locals())

@login_permission
def datatable_write(request):
    staff = get_user_login(request, Staff)
    #获取user表的所有数据
    return render(request, 'users/datatable_write.html', locals())
def search_handle(request):

    #查询所查询的关键字是否存在
    if not search_get(request) == None:
        user_list = search_get(request)
        data = dumps(user_list)

        return JsonResponse({'code':200,'data':data})
    else:
        return JsonResponse({'code':300})

def my_file(request):
    #定义可以上传的后缀
    file =request.FILES.get('file')
    #获取上传文件的后缀名
    file_type = file.name.split(".")
    file_type = file_type[-1]
    if file_type == 'csv':
        src  = 'static/upload/'+str(file.name)
        with open(src, 'wb') as csv_file:
            # 遍历网络传输过来的文件数据流,
            for c in file.chunks():
            # 将传输时候一段一段的数据存储到我们的 fname 中
                csv_file.write(c)
        file_json = dumps_csv(src)
        os.remove(src)
        return JsonResponse({'code':200,'data':file_json})
    else:
        return JsonResponse({'code': 300, 'data': '上传文件格式错误'})

def save_csv(request):
    data = json.loads(post(request,'data'))

    if save_csvs(data):
        return JsonResponse({'code': 200})
    else:
        return JsonResponse({'code':300})
@login_permission
def product_table(request):
    staff = get_user_login(request, Staff)
    product_list = Products.objects.filter(is_delete=False)
    paginator = Paginator(product_list, 20)
    # 获得当前的页码
    page = get(request, 'page')
    if not page:
        page = 1
    # 获得当前页码数据
    current_data = paginator.page(page)
    return render(request,'users/product.html',locals())

@login_permission
def pro_search(request):
    staff = get_user_login(request, Staff)
    #获取user表的所有数据
    return render(request, 'users/pro_search.html', locals())

@login_permission
def pro_up(request):
    staff = get_user_login(request, Staff)
    #获取user表的所有数据
    return render(request, 'users/pro_up.html', locals())
@login_permission
def sale_count(request):
    staff = get_user_login(request, Staff)
    #获取user表的所有数据
    data_dis = {}
    data_dis['year'] = get(request,'year')
    data_dis['mother'] = get(request, 'mother')
    data_dis['day'] = get(request, 'day')
    sale_data = search_sale(data_dis)
    #分页
    if sale_data !=None and sale_data!=[]:
            paginator = Paginator(sale_data, 20)
            # 获得当前的页码
            page = get(request, 'page')
            if not page:
                page = 1
            # 获得当前页码数据
            current_data = paginator.page(page)
    else:
        current_data= None
    return render(request, 'users/sales_table.html', locals())
@login_permission
def sales(request):
    staff = get_user_login(request, Staff)
    #获取user表的所有数据
    return render(request, 'users/sales.html', locals())
def pro_search_handle(request):
    #查询所查询的关键字是否存在
    if not pro_search_get(request) == None:
        user_list = pro_search_get(request)
        data = pro_dumps(user_list)
        return JsonResponse({'code':200,'data':data})
    else:
        print(123)
        return JsonResponse({'code':300})

def my_imgFile(request):
    #定义可以上传的后缀
    file =request.FILES.get('file')
    #获取上传文件的后缀名
    file_type = file.name.split(".")
    file_type = file_type[-1]
    src  = 'static/upload/'+str(file.name)
    with open(src, 'wb') as csv_file:
        # 遍历网络传输过来的文件数据流,
        for c in file.chunks():
        # 将传输时候一段一段的数据存储到我们的 fname 中
            csv_file.write(c)
    return JsonResponse({'code':200,'data':src})

def my_stock_up(request):
    data= json.loads(post(request,'data'))
    data['img']=makeNowdir(data['pro_img'])
    if check_pro(data):
        save_pro(data)
        return  JsonResponse({'code':200})
    else:
        return JsonResponse({'code':300})

def batch_upload(request):
    #定义可以上传的后缀
    file =request.FILES.get('file')
    #获取上传文件的后缀名
    file_type = file.name.split(".")
    file_name = file.name
    file_type = file_type[-1]

    if file_type == 'csv':
        src  = 'static/upload/'+str(file.name)
        with open(src, 'wb') as csv_file:
            # 遍历网络传输过来的文件数据流,
            for c in file.chunks():
            # 将传输时候一段一段的数据存储到我们的 fname 中
                csv_file.write(c)
        file_json = dumps_csv2(src)
        if(file_json == None):
            return JsonResponse({'code': 300, 'data': '上传文件格式错误'})
        else:
            file_len = len(file_json)
            return JsonResponse({'code':200,'data':file_name,'lens':file_len})
    else:
        return JsonResponse({'code': 300, 'data': '上传文件格式错误'})

def Bulk_img(request):
    file = request.FILES.get('img')
    src = 'static/bulk_img/' + str(file.name)
    file_type = file.name.split(".")
    file_type = file_type[-1]
    if file_type == 'png' or file_type == 'jpg':
        with open(src, 'wb') as img_file:
            # 遍历网络传输过来的文件数据流,
            for c in file.chunks():
                # 将传输时候一段一段的数据存储到我们的 fname 中
                img_file.write(c)
        return JsonResponse({'code': 200, 'data': '上传文件成功'})
    else:
        return JsonResponse({'code': 300, 'data': '上传文件格式错误'})


def bulk_pagination(request):
#获取上传后的数据
    file_name= get(request,'file_name')
    start = get(request,'start')
    page_limit = get(request,'limit')
    data = load_bulk(file_name,start,page_limit)
    json_data = dumps_list(data)
    return JsonResponse({'code': 200, 'data': json_data})


def bulk_save(request):
    file_name = post(request,'file_name')
    flag = bulk_save_sql(file_name)
    src= 'static/upload/'+file_name
    os.remove(src)
    if flag:
        return JsonResponse({'code': 200})
    else:
        return JsonResponse({'code': 300,'data':'部分内容因为重复并没有成功上传请检查后重新上传'})

def one_sale_save(request):
    pid= post(request,'pid')
    out = post(request,'out')
    stock = sale_save(pid,out)
    if stock:
        return JsonResponse({'code': 200,'data':stock})
    else:
        return JsonResponse({'code': 300, 'data': '失败'})

def bulk_sale(request):
    #定义可以上传的后缀
    file =request.FILES.get('file')
    #获取上传文件的后缀名
    file_type = file.name.split(".")
    file_type = file_type[-1]
    if file_type == 'csv':
        src  = 'static/upload/'+str(file.name)
        with open(src, 'wb') as csv_file:
            # 遍历网络传输过来的文件数据流,
            for c in file.chunks():
            # 将传输时候一段一段的数据存储到我们的 fname 中
                csv_file.write(c)
        file_json = dumps_csv3(src)
        print(src)
        if file_json:
            os.remove(src)
            return JsonResponse({'code':200,'data':file_json})
        else:
            return JsonResponse({'code': 300, 'data': '上传文件格式错误'})
    else:
        return JsonResponse({'code': 300, 'data': '上传文件格式错误'})

def bulk_sale_save(request):
    data = json.loads(post(request,'data'))
    if bulk_sale_save_fu(data):
        return JsonResponse({'code':200})
    else:
        return JsonResponse({'code': 300})


def down_load(request):
    data_dis = {}
    data = json.loads(post(request, 'data'))
    try:
        data_dis['year'] =data['year']
        data_dis['mother'] =data['mother']
        data_dis['day'] = data['day']
        file_name = 'data'+str(time.time())+'.csv'
        sale_data = search_sale(data_dis)

        if sale_data != None and sale_data != []:
            print(sale_data)
            src = 'static/upload/'+file_name
            with open(src,'w') as csv_file:
                fieldnames = ['name', 'out', 'pid']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for i in sale_data:
                    writer.writerow({'name': i['name'], 'out': i['out'],'pid':i['pid']})
            return JsonResponse({'code':200,'data':file_name})
        else:
            return JsonResponse({'code':300,'data':'导出数据为空'})
    except Exception as e:
        print(e)

# def func(pro):
#     stock = Storage.objects.filter(sto_pro_id=pro.id).last().sto_stock

@login_permission
def sto_search(request):
    # 获取user表的所有数据
    staff = get_user_login(request, Staff)
    pro = Products.objects.all()
    list_pro = list(pro)
    pro = sorted(list_pro, key=lambda x:Storage.objects.filter(sto_pro_id=x.id).last().sto_stock if Storage.objects.filter(sto_pro_id=x.id)  else 0 , reverse=True)
    paginator = Paginator(pro, 30)
    # 获得当前的页码
    page = get(request, 'page')
    if not page:
        page = 1
    # 获得当前页码数据
    current_data = paginator.page(page)
    return render(request, 'users/sto_search.html', locals())
# curl -X POST -H
# "AppKey: go9dnk49bkd9jd9vmel1kglw0803mgq3" -H "
# CurTime: 1443592222" -H "CheckSum: 9e9db3b6c9abb2e1962cf3e6f7316fcc55583f86" -H
# "Nonce: 4tgggergigwow323t23t" -H "Content-Type: application/x-www-form-urlencoded" -d
# 'mobile=13812345678' 'https://api.netease.im/sms/sendcode.action'
def get_phone(request):
    cache.set('key','value',30)
    print(cache.get('key'))
    url = 'https://api.netease.im/sms/sendcode.action'
    headers={'Content-Type':'application/x-www-form-urlencoded'}
    CurTime = str(int(time.time()))
    print(CurTime)
    APP_SECRET = 'fc3ef386ef8b'
    NONCE = "123456"
    TEMPLATEID = "3057527"
    MOBILE = "17621478391"
    CODELEN='4'
    CheckSum = CheckSum_en(APP_SECRET+NONCE+CurTime)
    print(CheckSum)
    headers = {'AppKey':'8b120bdde8c88b62707ddc1811b23784', 'CurTime': CurTime,'Nonce':NONCE,
               'CheckSum':CheckSum,'Content-Type':"application/x-www-form-urlencoded;charset=utf-8"}
    payload={'mobile':MOBILE,'codeLen':CODELEN}
    r= requests.post(url,headers=headers,data=payload)
    print(r.text)
    return HttpResponse(r.text)