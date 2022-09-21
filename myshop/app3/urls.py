from django.urls import path
from app3 import views

urlpatterns = [
    path('var/', views.var),
    path('diy_filter/', views.diy_filter),
    path('diy_tags/', views.diy_tags),
    path('welcome/', views.welcome),
]