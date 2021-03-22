from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from common.models import Customer


def listcustomers(request):
    qs = Customer.objects.values()
    resStr = ''
    for customer in qs:
        for name,value in customer.items():
            resStr += f'{name}:{value}|'
        resStr += '<br>'
    return HttpResponse(resStr)