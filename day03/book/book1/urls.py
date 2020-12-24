from django.urls import path
from book1.views import index
urlpatterns = [
    path("index/", index),
]
