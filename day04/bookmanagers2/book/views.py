from django.shortcuts import render
from book.models import BookInfo,PeopleInfo
from django.http.response import HttpResponse
# 1.1 由一到多的访问语法:一对应的模型类对象.多对应的模型类名小写_set
# 1. 获取书籍信息
book = BookInfo.objects.get(id=1)
# 2.根据书籍信息获取人物信息
# models.Model 父类会根据外键关系 自动给我们的模型类添加属性(字段)
# peopelinfo_set 指向了 人物信息
# .all() 表示获取所有数据
book.peopleinfo_set.all()
# 1.2 由多到一的访问语法:多对应的模型类对象.多对应的模型类中的关系类属性名 例
from book.models import PeopleInfo
# 1.查询人物信息
from book.models import PeopleInfo
# 1.查询人物信息
person=PeopleInfo.objects.get(id=6)
# 2.根据人物信息 获取书籍相关联的信息
# person.book 这个实例对象 是系统根据级联关系,帮助我们生成的
person.book
# person.实例对象
# person.book = BookInfo()
# 2.根据人物信息 获取书籍相关联的信息
# person.book 这个实例对象 是系统根据级联关系,帮助我们生成的
person.book
# person.实例对象
# person.book = BookInfo()
# 2.1 由多模型类条件查询一模型类数据:
# 语法如下:
# 关联模型类名小写__属性名__条件运算符=值
# 模型类名.objects.filter(关联模型类名小写__属性值__运算符=值)
BookInfo.objects.filter(peopleinfo__description__contains="八")
# 查询图书,要求图书人物为"郭靖"
BookInfo.objects.filter(peopleinfo__name='郭靖')
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
# Create your views here.
# 2.2 由一模型类条件查询多模型类数据:
# 语法如下:
# 一模型类关联属性名__一模型类属性名__条件运算符=值
# 1. 明确需要的数据
# 2. 添加条件
# 模型类名.objects.filter(外键__属性值__运算符=值)
# 查询图书阅读量大于30的所有人物
from book.models import PeopleInfo
PeopleInfo.objects.filter(book__readcount__gt=30)
# 查询书名为“天龙八部”的所有人物
PeopleInfo.objects.filter(book__name__exact="天龙八部")
# 分页查询
# 1.导入分页类
from django.core.paginator import Paginator
# 2. 查询结果集
people=PeopleInfo.objects.all()
# 3. 创建分页类
# object_list, 列表数据
# per_page 每页多少条数据
paginator=Paginator(object_list=people,per_page=2)
# 4. 获取分页
persons=paginator.page(1)
persons.object_list
# 5. 获取分页总数
paginator.num_pages


def index(request):
    return HttpResponse("哈哈哈")


def book(request, cat_id, detail_id):
    #######################QueryDict############################
    # http://127.0.0.1:8000/1/100/?a=10&b=20&a=666
    # print(query_string)
    # < QueryDict: {'a': ['10', '666'], 'b': ['20']} >
    """
    QueryDict
    可以 一键一值 也可以一键多值
    一键一值 : QueryDict_data.get(key)
    一键多值 : QueryDict_data.getlist(key)
    """
    print(cat_id, detail_id)
    query_string = request.GET
    alist = query_string.getlist("a")
    b = query_string.get("b")
    print(alist, b)

    return HttpResponse("好好好")


# POST请求————表单类型 FromData（重点）
# 请求链接：127.0.0.1:8000/login/
def login(request):
    # 获取参数
    body = request.POST
    print(body)
    return HttpResponse('login')


# POST请求————非标单类型Non-FOrm Data(重点)
# s设置postman
def weibo(request):
    # JSON数据的接收是在request.body中
    # 接收数据
    body = request.body
    print(body)
    # b'{\n    "name":"itcast",\n    "age":"18"\n}'
    # 将bytes类型的数据转换为str类型
    body_str = body.decode()
    print(body_str)
    # {
    #     "name":"itcast",
    #     "age":"18"
    # }
    # 这是JSON的字符串形式
    # 需要将JSON的字符串形式转化为字典
    import json
    data = json.loads(body_str)
    a = data["name"]
    b = data["age"]
    print(a,b)
    return HttpResponse("weibo")