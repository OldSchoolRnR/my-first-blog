from django.conf.urls import *
from . import views

urlpatterns = [
    url('', views.post_list, name='post_list'),
]