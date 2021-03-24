from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout


# 管理员登录界面的！

def signIn(request):
    # 从HTTP POST请求中 获取用户名和密码
    # 把提交的数据放置在HTTP包的包体中
    userName = request.POST.get('username')
    password = request.POST.get('password')

    # 使用auth库里的方法校验用户名密码
    user = authenticate(username=userName, password=password)

    # 如果能找到用户名并且密码正确
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # 在session中存入用户类型
                request.session['usertype'] = 'mgr'

                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': '请使用管理员账户登录'})
        else:
            return JsonResponse({'ret': 0, 'msg': '用户已经被禁'})
    else:
        return JsonResponse({'ret': 1, 'msg': '用户名或密码错误'})


# 登出：
def signOut(request):
    logout(request)
    return JsonResponse({'ret': 0})
