from django.http import JsonResponse
import json


# 定义一个区分方法的函数
def dispatcher(request):
# if部分用来区分前端给后端的数据类型（一个信号 / 带着数据的），最终格式都是字典格式的

    # 如果GET，就把？后面的参数给params（GET是前端向后端要数据，给一个信号向后端要数据）
    if request.method == 'GET':
        request.params = request.GET

    # 如果[],则从request.body取出数据给params（[]是前端给后端数据，带着数据来的）
    elif request.method in ['POST','PUT','DELETE']:
        # request.body获取json字符串，json.load是把json字符串变成json对象（python可编辑查找的格式）
        request.params = json.loads(request.body)


# 根据不同方法派发不同函数处理
    # action是前端给后端信息中的一个参数，以表示方法
    action = request.params['action']
    if action == 'list_customer':
        return listCustomers(request)
    elif action == 'add_customer':
        return addCustomer(request)
    elif action == 'modify_customer':
        return modifyCustomers(request)
    elif action == 'delete_customer':
        return deleteCustomer(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型的http请求'})


