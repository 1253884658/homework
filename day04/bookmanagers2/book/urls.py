from django.urls import path
from book.views import index,book,login,weibo
urlpatterns = [
    path('index/', index),
    # 1/100/
    # path('1/100/',book),
    path('<cat_id>/<detail_id>/', book),
    # 相当于 cat_id=1<> 符号
    # 相当于 detail_id=100
    path('login/', login),
    path('weibo/',weibo),
]