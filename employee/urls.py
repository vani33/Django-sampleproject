from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    
    path("homepage",views.homepage, name="homepage"),
    path("register",views.register, name="register"),
    path("login",views.login, name="login")
]

