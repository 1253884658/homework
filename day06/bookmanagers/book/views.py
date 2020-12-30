from django.shortcuts import render
from django.http.response import HttpResponse


# 面向过程视图函数的定义
def test(request):
    # 打印请求方法
    print(request.method)
    if request.method == "GET":
        return HttpResponse('get')
    else:
        return HttpResponse('post')


# 类视图的定义
# 类视图继承自view
# 类视图的方法是根据  请求方式来实现的
# 如果我们用 post 发送了一个 get请求, 我们就实现类视图中 get方法
# 如果我们用 post 发送了一个 post请求, 我们就实现类视图中 post方法
from django.views import View


class JDLogin(View):
    def get(self, request):
        return HttpResponse("京东 GET")

    def post(self, request):
        return HttpResponse("京东 POST")


# 类视图的多继承重写dispath
"""
如果我们访问 个人中心页面,必须要求用户登录
1.定义个人中心类视图
2.必须要求用户登录 (我们后边会讲解如何判断用户是否登录,我们现在先模拟假的)
"""


class CenterView(View):
    def get(self, request):
        islogin = False
        if islogin:
            # 展示个人信息
            return HttpResponse("center get")
        else:
            return HttpResponse("请登录")

    def post(self, request):
        islogin = False
        if islogin:
            # 修改个人信息
            return HttpResponse("center post")
        else:
            return HttpResponse("请登录")


from django.contrib.auth.mixins import LoginRequiredMixin


class CenterView1(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse("center get")

    def post(self, request):
        return HttpResponse("center post")
