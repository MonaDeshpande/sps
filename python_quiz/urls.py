from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('home/', home),
    path('admin_login/', admin_login),
    path('add_administrator/', add_administrator),
]