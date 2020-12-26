from django.urls import path
from book.views import index,book,index1,login,weibo
urlpatterns = [
    path('index/', index),
    path('<cat_id>/<detail_id>/', book),
    path("index1/", index1),
    path('login/', login),
    path('weibo/',weibo)
]