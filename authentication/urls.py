# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, logout_view

urlpatterns = [
    path('', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", logout_view, name="logout"),
]
