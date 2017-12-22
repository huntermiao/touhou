# -*-coding:utf-8 -*-

from django.template import Library
from normal_user.models import *

register = Library()


#对获取的当年的数据进行过滤
@register.filter
def user_consumption(user):
    con = user.consumption_set.filter(con_year='2017')
    if con:
        #初始化价格参数
        price = 0
        for co in con:
            price+=int(co.con_pro.pro_price)*int(co.con_nums)
        return price
    else:
        return 0


@register.filter
def my_sto_out(pro):
    sto = pro.storage_set.filter(is_delete=False)
    out = 0
    for i in sto:
        out+=i.sto_out
    return out
@register.filter
def sto_before(pro):
    sto = pro.storage_set.filter(is_delete=False)
    if(sto.first()):
        stock = sto.first().sto_stock
    else:
        stock = 0
    return stock