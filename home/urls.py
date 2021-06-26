#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from . import views 


app_name='home'
urlpatterns = [
    path('', views.TemplateView.as_view(template_name = 'home/main.html')),
]
