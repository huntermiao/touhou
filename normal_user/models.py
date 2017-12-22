from django.db import models
from db.BaseModel import *
from utils.wrappers import *
from utils.common import *
from tinymce.models import HTMLField
# Create your models here.


# class Normal_user(BaseModels):
#     userName = models.CharField(max_length=20) #用户名
#     passWord =models.CharField(max_length=255) #用户密码
#     registeredTime = models.DateField(null=True) #用户注册时间
#     nickname = models.CharField(max_length=16,null=True) #用户昵称
#     signature = models.CharField(max_length=255,null=True) #用户个人签名
#     birthDate = models.DateField() #用户生日
#     gender  = models.CharField(max_length=1,default=0) # 用户性别
#     avatar = models.ImageField()

class StaffManager(models.Manager):

    # 根据用户名查询用户
    def get_userinfo_by_name(self, staff_name):
        try:
            return self.get(staff_name=staff_name)
        except Staff.DoesNotExist:
            return None

    # 注册信息入库
    def register_userinfo_save(self, request):

        # 获取表单数据
        staff_name = post(request, 'user_name')
        staff_pass = post(request, 'pass_word')
        staff_phone = post(request, 'phone_num')

        staff = Staff()
        staff.staff_name = staff_name
        staff.staff_pass = password_encryption(staff_pass)
        staff.staff_phone = staff_phone
        # 保存数据
        staff.save()







class User(BaseModels):
    #用户表
    user_name = models.CharField(max_length=20,verbose_name='用户名') #用户名
    user_num = models.CharField(max_length=20,null=True,verbose_name='会员号') #会员号
    user_pass = models.CharField(max_length=64,verbose_name='用户密码')
    user_marriage = models.CharField(max_length=6,default='未知',verbose_name='婚姻状况') #婚姻状况
    user_phone = models.CharField(max_length=11,null=True,verbose_name='用户手机') #用户手机
    user_birth = models.CharField(max_length=20,verbose_name='用户生日') #用户生日
    user_address = models.CharField(max_length=255,verbose_name='用户地址') #用户住址
    user_age = models.CharField(max_length=3,default='保密',verbose_name='会员年龄')
    # objects = UserManager()
    def __str__(self):
        return self.user_name

class Staff(BaseModels):
    #店员表
    staff_name = models.CharField(max_length=20, verbose_name='员工姓名')  # 员工姓名
    staff_num = models.CharField(max_length=20, null=True, verbose_name='员工编号')  # 员工编号
    staff_pass = models.CharField(max_length=64, verbose_name='员工密码')
    staff_phone = models.CharField(max_length=11, null=True, verbose_name='员工手机')  # 员工手机
    staff_address = models.CharField(max_length=255, verbose_name='员工住址')  # 员工住址
    staff_img = models.ImageField(default=None)
    staff_permissions = models.BooleanField(default=False) #管理员权限


    objects = StaffManager()

class Cources(BaseModels):
    #服务
    cource_name = models.CharField(max_length=20, verbose_name='服务名称')
    cource_price = models.IntegerField(default=0,verbose_name='服务价格')


# 商品分类模型
class ProductsCategory(BaseModels):

    # 商品分类名称
    pro_name = models.CharField(max_length=20)
    # 商品分类样式
    pro_css = models.CharField(max_length=20)
    # 商品分类图片
    pro_image = models.ImageField()

class Products(BaseModels):
    #产品
    pro_name = models.CharField(max_length=20, verbose_name='产品名称')
    pro_price = models.IntegerField(default=0,verbose_name='产品价格')
    pro_num= models.CharField(max_length=30,verbose_name='产品编号')
    pro_img = models.ImageField(default=None,verbose_name='产品图片')
    # 商品概述
    pro_short = models.CharField(max_length=100)
    # 商品描述
    pro_desc = HTMLField()
    pro_units = models.CharField(max_length=10,verbose_name='产品单位',default='/个')
    pro_sale = models.IntegerField(default=0)
    pro_type = models.ForeignKey(ProductsCategory)

class Storage(BaseModels):
    #库存
    sto_time = models.DateField(auto_now_add=True,verbose_name='修改时间')
    sto_stock = models.IntegerField(default=0,verbose_name='库存')
    sto_out = models.IntegerField(default=0,verbose_name='出库')
    sto_into = models.IntegerField(default=0,verbose_name='入库')
    sto_pro = models.ForeignKey(Products,verbose_name='产品id')




class ProductsImages(BaseModels):

    # 图片路径
    img_url = models.CharField(max_length=50)
    # 所属商品
    img_goods = models.ForeignKey(Products)


class Consumption(BaseModels):
    #消费记录
    #消费时间
    con_year = models.CharField(max_length=4,verbose_name='创建年份')
    con_month = models.CharField(max_length=2, verbose_name='创建月份')
    con_day = models.CharField(max_length=2, verbose_name='创建日期')
    # 购买商品数量
    con_nums = models.IntegerField()
    #所属用户
    con_pro = models.ForeignKey('Products') #pid
    con_user = models.ForeignKey('User')

    def __str__(self):
        return  self.con_nums