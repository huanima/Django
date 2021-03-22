from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from common.models import Customer


def listcustomers(request):
    # qs是获得全部数据
    qs = Customer.objects.values()

    # 根据request筛选
    ph = request.GET.get('phoneNumber',None)        #GET是把？后整个取出来，get是把''的部分取出，例如'phoneNumber=1234567'
    if ph:
        qs = qs.filter(phoneNumber=ph)

    # 输出格式
    resStr = ''
    for customer in qs:
        for name,value in customer.items():
            resStr += f'{name}:{value}|'
        resStr += '<br>'
    return HttpResponse(resStr)