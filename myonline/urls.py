#!/usr/bin/python
# coding=utf-8

from django.conf.urls import url
from . import views

app_name='myonline'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
    ]