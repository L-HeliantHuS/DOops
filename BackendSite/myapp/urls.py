#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ Author: HeliantHuS
@ Codes are far away from bugs with the animal protecting
@ Time:  2019/12/23
@ FileName: urls.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path("ping", views.Ping),
    path("user/error", views.Error),
    path("user/login", views.Login),
    path("user/logout", views.Logout),
    path("user/isLogin", views.isLogin), # 判断是否登录
    path("hosts", views.TestHosts), # 检测当前存活主机
    path("host", views.Host),   # 主机的crud
    path("group", views.CrudGroup),  # 组的crud
    path("exec", views.Exec),
    path("auth", views.AuthConf),

    path("status", views.Status)
]
