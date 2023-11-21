from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('home/', home),
    path('Admin_login/', admin_login),
]