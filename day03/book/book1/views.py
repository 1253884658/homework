from django.db.models import F, Q
from django.shortcuts import render
from django.http.response import HttpResponse
from book1.models import BookInfo,PeopleInfo
# Create your views here.


def index(request):
    return HttpResponse('哈哈哈')


# 增加数据
book = BookInfo(
    name='python入门',
    pub_date='2010-1-1',
)
book.save()

PeopleInfo.objects.create(
    name='itheima',
    book=book
)
# 修改
# save()
person = PeopleInfo.objects.get(name='itheima')
person.name = 'itcast'
person.save()
# update
PeopleInfo.objects.filter(name="itcast").update(name="传智播客")
# 删除
# 模型类.objects.filter.delete()
person = BookInfo.objects.filter(name="python入门").delete()
# 模型类对象delete

person = PeopleInfo.objects.get(name="传智播客")
person.delete()
# 基础条件查询
# get查询单一结果，如果不存在，会抛出异常。
# all查询多个结果
# count查询结果数量
BookInfo.objects.get(id=1)
BookInfo.objects.all()
# 过滤查询
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果


# 查询编号为1的图书
BookInfo.objects.get(id=1)
BookInfo.objects.filter(id=1)

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains="湖")
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith="部")
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 3, 5])
# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt="1990-1-1")
# F和Q对象
# F对象
# 之前的查询都是对象的属性与常量值比较，两个属性怎么比较呢？
# 例：查询阅读量大于等于评论量的图书。
BookInfo.objects.filter(readcount__gt=F('commentcount'))
# 可以在F对象上使用算数运算。
# 例：查询阅读量大于2倍评论量的图书。
BookInfo.objects.filter(readcount__gt=F('commentcount')*2)
# Q对象
# 多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字。
# 例：查询阅读量大于20，并且编号小于3的图书。
BookInfo.objects.filter(readcount__gt=20,id__lt=3)
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
# 如果需要实现逻辑或or的查询，需要使用Q()对象结合|运算符，Q对象被义在django.db.models中。
# 例：查询阅读量大于20的图书，改写为Q对象如下。
BookInfo.objects.filter(Q(readcount__gt=20))
# Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或。
# 例：查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
# Q对象前可以使用~操作符，表示非not。
# 例：查询编号不等于3的图书。
BookInfo.objects.filter(~Q(id__lt=3))
# 使用aggregate()过滤器调用聚合函数。聚合函数包括：Avg平均，Count数量，Max最大，Min最小，Sum求和，被定义在django.db.models中。
# 例：查询图书的总阅读量。
from django.db.models import Sum,Max,Min,Avg,Count
BookInfo.objects.aggregate(Sum("readcount"))
# 使用count时一般不使用aggregate()过滤器。
#
# 例：查询图书总数。
BookInfo.objects.count()
# 排序
# 使用order_by对结果进行排序
# 默认升序
BookInfo.objects.all().order_by('readcount')
# 降序
BookInfo.objects.all().order_by("-readcount")





