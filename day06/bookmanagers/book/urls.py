from django.urls import path
from book.views import test ,JDLogin,CenterView
from django.urls import register_converter
urlpatterns = [
    path("test/", test),
    # 类视图的url
    # path 的第一个参数   url
    # path 的第二个参数   视图函数的名字
    path("jd/",JDLogin.as_view()),
    path("center/",CenterView.as_view())

]
