from django.test import TestCase
from .models import *
import random



# categories = [
#     {'goods_name': '新鲜水果', 'goods_css': 'fruit', 'goods_image': 'images/banner01.jpg'},
#     {'goods_name': '海鲜水产', 'goods_css': 'seafood', 'goods_image': 'images/banner02.jpg'},
#     {'goods_name': '猪牛羊肉', 'goods_css': 'meet', 'goods_image': 'images/banner03.jpg'},
#     {'goods_name': '禽类蛋品', 'goods_css': 'egg', 'goods_image': 'images/banner04.jpg'},
#     {'goods_name': '新鲜蔬菜', 'goods_css': 'vegetables', 'goods_image': 'images/banner05.jpg'},
#     {'goods_name': '速冻食品', 'goods_css': 'ice', 'goods_image': 'images/banner06.jpg'},
# ]
#
#
# for cag in categories:
#
#     c = ProductsCategory()
#     c.pro_name = cag['goods_name']
#     c.pro_css = cag['goods_css']
#     c.pro_image = cag['goods_image']
#     c.save()


# 创建商品数据
# units = ['1个', '1头', '1坨', '1吨', '1克', '500克', '2箱', '1车', '10条']
# with open('/home/huntermiao/myWork/touhou/data.txt', 'r') as f:
#     for name in f:
#         # 创建商品对象
#         g = Products()
#         g.pro_name = name[:-1]
#         g.pro_price = random.randint(100, 999)
#         g.pro_type_id = random.randint(1, 6)
#         g.pro_desc = '商品非常好，价格便宜，童叟无欺哦!'
#         g.pro_short = '商品真的是非常好啊，日销量过万，在不买就没了!'
#         g.pro_img = 'goods/' + str(random.randint(1, 18)) + '.jpg'
#         g.pro_sale = 0
#         g.pro_units = units[random.randint(0, len(units) - 1)]
# #         g.save()
# users = [
#     {'user_name': '老王', 'user_num': '006', 'user_phone': '119'},
#     {'user_name': '老李', 'user_num': '007', 'user_phone': '110'},
#     {'user_name': '老张', 'user_num': '008', 'user_phone': '114'},
#     {'user_name': '老四', 'user_num': '009', 'user_phone': '112'},
#     {'user_name': '老杨', 'user_num': '010', 'user_phone': '10086'},
#
# ]
#
#
# for use in users:

# c = User()
# c.user_name = 'hunter'
# c.user_num = '一号'
# c.user_phone = 'yello'
# c.save()


# consumption =[
#     {'con_year':'2017','con_month':'7','con_day':'20','con_nums':'10','con_pro':10,'con_user':2},
#     {'con_year':'2017','con_month':'7','con_day':'12','con_nums':'2','con_pro':9,'con_user':2},
#     {'con_year':'2017','con_month':'7','con_day':'11','con_nums':'1','con_pro':1,'con_user':2},
#     {'con_year':'2017','con_month':'7','con_day':'1','con_nums':'1','con_pro':2,'con_user':2},
#     {'con_year':'2017','con_month':'7','con_day':'2','con_nums':'2','con_pro':3,'con_user':2},
#     {'con_year':'2017','con_month':'7','con_day':'3','con_nums':'3','con_pro':4,'con_user':2},
#     {'con_year':'2017','con_month':'7','con_day':'4','con_nums':'4','con_pro':5,'con_user':2},
#     {'con_year':'2017','con_month':'7','con_day':'5','con_nums':'5','con_pro':6,'con_user':2},
#     {'con_year':'2017','con_month':'7','con_day':'6','con_nums':'6','con_pro':7,'con_user':2},
#     {'con_year':'2017','con_month':'7','con_day':'7','con_nums':'7','con_pro':8,'con_user':2},
# ]
#
# for con in consumption:
#
#     c = Consumption()
#     c.con_year = con['con_year']
#     c.con_day = con['con_day']
#     c.con_month = con['con_month']
#     c.con_nums = con['con_nums']
#     c.con_pro_id = con['con_pro']
#     c.con_user_id = con['con_user']
#     c.save()


c = Storage()
c.sto_into = 3000
c.sto_pro_id=1
c.sto_out = 0
c.sto_stock = c.sto_into - c.sto_out
c.save()


