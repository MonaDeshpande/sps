from django.contrib import admin
from django.urls import path
from . import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home),
    path('admin_login/', admin_login),
    path('add_administrator/', add_administrator),
    path('admin/', views.administrator_form_register.view.as_view(), name = 'home'),
]+ static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)