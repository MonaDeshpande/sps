from django.contrib import admin
from django.urls import path
from . import views
from .views import*

urlpatterns = [
    path('guess_number_user/', guess_number_user),
    # path('admin_login/', admin_login),
]