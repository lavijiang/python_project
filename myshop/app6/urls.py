from django.urls import path
from app6 import views

urlpatterns = [
    path('reg/', views.user_reg),
]