from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('', students_home),
    path('students_data', students_data),
    path('add_students', add_students),
]
