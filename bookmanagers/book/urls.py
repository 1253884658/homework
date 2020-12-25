from django.urls import path
from book.views import index,post,weibo
urlpatterns = [
    path('<cat_id>/<detail_id>/', index),
    path('post/', post),
    path('weibo/', weibo)
]
