from django.urls import path
from hero.views import index
urlpatterns = [
    path("index/", index),
]