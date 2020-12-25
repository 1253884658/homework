from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def index(request,cat_id,detail_id):
    # print(cat_id,detail_id)
    query_string = request.GET
    a = query_string.getlist('a')
    b = query_string.get('b')
    print(a,b)
    return HttpResponse("哈哈哈")


# 请求体
# 表单类型 Form Data
def post(request):
    # POST请求
    # 接收form_data数据的属性
    body = request.POST
    print(body)
    # <QueryDict: {'user': ['han'], 'password': ['123']}>
    a = body.get('user')
    b = body.get('password')
    print(a,b)
    return HttpResponse('哈哈哈')


# POST请求————非表单类型Non-Form Data
def weibo(request):
    # JSON数据接收是在request.body中
    # 1.参数接收
    body = request.body
    print(body)
    # b'{\n\t"name":"itcast"\n\t"age":"18"\n}'
    # 2.将bytes类型的数据转换为str类型
    body_str = body.decode()
    print(body_str)
    # body_str不是Python的字典，是JSON的字符串
    # 3.需要将JSON形式的字符串转化为字典
    import json
    data = json.loads(body_str)
    print(data)

    return HttpResponse('微博')