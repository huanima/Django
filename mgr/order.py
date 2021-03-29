from django.http import JsonResponse
import json
from common.models import Order,OrderMedicine


# 这里讲的是 前端对manager的四个操作用同一个路由，如何分流和增删改查（区分前后端）


# 1.把校验管理员，放在区分方法的函数里！
# 定义一个区分方法的函数
def dispatcher(request):
    if 'usertyle' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未登录',
            'redirect':'/mgr/sign.html'},
        status = 302)

    if request.session['usertype'] != 'mgr':
        return JsonResponse({
            'ret': 302,
            'msg': '用户非mgr类型',
            'redirect': '/mgr/sign.html'},
        status = 302)






# 2.if部分用来区分前端给后端的数据类型（一个信号 / 带着数据的），最终格式都是字典格式

    # 如果GET，就把？后面的参数给params（GET是前端向后端要数据，给一个信号向后端要数据）
    if request.method == 'GET':
        request.params = request.GET

    # 如果[],则从request.body取出数据给params（[]是前端给后端数据，带着数据来的）
    elif request.method in ['POST','PUT','DELETE']:
        # request.body获取json字符串，json.load是把json字符串变成python里的字典对象
        request.params = json.loads(request.body)







# 根据不同方法派发不同函数处理
    # action是前端给后端信息中的一个参数，以表示方法
    action = request.params['action']
    if action == 'list_order':
        # 对于get，？后面有 action = list_customer
        return listOrder(request)
    elif action == 'add_order':
        return addOrder(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型的http请求'})







# 处理get的函数（获取）
def listOrder(request):
    # 获得common.models的Customer的所有数据
    qs = Order.objects.values()
    # 把qs的格式转化为list
    retlist = list(qs)
    # 补全剩余部分，JsonResponses是用Json格式输出，ret=0代表成功
    return JsonResponse({'ret': 0, 'retlist': retlist})







# 例子1：前端向后端添加的用户信息
# {
#     "action":"add_customer",
#     "data":{
#         "name":"小尿泡",
#         "phoneNumber":"133",
#         "address":"133"
#     }
# }

# 处理post的函数（添加）
def addOrder(request):
    # request.params里已经包含前端给后端的数据了，现在request.params是字典格式，data是数据所在的key（人定义的名字啦）
    info = request.params['data']

    # record（也就是create的返回值）是新添加的这一行
    record = Order.objects.create(name=info['name'],
                            phoneNumber=info['phoneNumber'],
                            address=info['address'])

    # record.id是添加这一行的序号，返回给前端
    return JsonResponse({'ret': 0, 'id': record.id})






