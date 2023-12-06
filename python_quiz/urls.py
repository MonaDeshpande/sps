from django.contrib import admin
from django.urls import path
from . import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home),
    path('admin_login/', admin_login),
    path('admin_details/', admin_details),
    path('delete/<int:admin_id>', delete_admin),
    path('update/<int:admin_id>', update_admin),
    # path('admin/', views.formView.as_view(), name = 'home'),
    # path('admin/', formView),
    
    
]+ static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)