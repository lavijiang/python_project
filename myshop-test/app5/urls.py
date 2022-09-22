from django.urls import path
from app5 import views

urlpatterns = [
    path('upload_file/', views.upload_file),
    path('ajax_login/', views.ajax_login),
    path('ajax_login_data/', views.ajax_login_data),
]