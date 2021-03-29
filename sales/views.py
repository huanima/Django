from django.shortcuts import render

# Create your views here.

#这讲的是 把客户信息 通过电话条件筛选 并输出这一行（是一种没区分前后端的处理）

from django.http import HttpResponse
from common.models import Customer


def listcustomers(request):
    # qs是获得全部数据
    qs = Customer.objects.values()

    # 根据request筛选
    # GET是把？后整个取出来，get是把''的部分除表头部分取出来，例如对于？phoneNumber=1234567，输出的是 ph = 1234567
    ph = request.GET.get('phoneNumber',None)
    if ph:
        qs = qs.filter(phoneNumber=ph)


    # 输出格式
    resStr = ''
    for customer in qs:
        for name,value in customer.items():
            resStr += f'{name}:{value}|'
        resStr += '<br>'
    return HttpResponse(resStr)