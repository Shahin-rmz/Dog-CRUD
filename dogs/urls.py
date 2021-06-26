#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from pywebio.platform.django import webio_view
from django.contrib.auth.decorators import login_required

from .pywebio_app1 import page1
from .pywebio_app2 import page2


webio_view_func1 = login_required(webio_view(page1))
webio_view_func2 = login_required(webio_view(page2))

urlpatterns = [
    path('',webio_view_func1),
    path('pg2',webio_view_func2)
]
