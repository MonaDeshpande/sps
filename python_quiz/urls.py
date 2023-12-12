from django.contrib import admin
from django.urls import path
from . import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home),
    path('admin_signup/', admin_login),
    path('admin_details/', admin_details),
    path('delete/<str:email_id>', delete_admin),
    path('update/<str:email_id>', update_admin),
    path('signin/', sign_in),
    path('add_questions/', add_questions),
    path('questions/', questions),
    path('question_details/', question_details),
    path('question_delete/<str:question>', delete_question),
    path('question_update/<str:question>', update_question)
    # path('admin/', views.formView.as_view(), name = 'home'),
    # path('admin/', formView),
    
    
]+ static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)