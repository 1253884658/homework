from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('哈哈')


# GET请求————URL路径参数
# 请求链接：127.0.0.1:8000/1/100/
def book(request, cat_id, detail_id):
    print(cat_id, detail_id)
    return HttpResponse(detail_id)


# GET请求--Query String
# 请求链接：127.0.0.1:8000/index1/?a=10&b=20&a=666
def index1(request):
    query_string = request.GET
    a = query_string.getlist('a')
    b = query_string.getlist('b')
    print(a, b)
    return HttpResponse("测试")


# POST请求--表单类型From Data
# 配置系统设置
def login(request):
    body = request.POST
    print(body)
    return HttpResponse("login")


# POST请求--非标单类型NOn-Form Data
# 配置postman
# 请求链接：127.0.0.1:8000/weibo/
def weibo(request):
    body = request.body
    print(body)
    # 转化为字符串类型
    body_string = body.decode()
    # 这时该字符串为JSON类型的字符串
    import json
    data = json.loads(body_string)
    print(data)
    a = data["name"]
    b = data["age"]
    print(a, b)
    return HttpResponse('微博')