from django.urls import path
from app2 import views
from app2.views_class import *

urlpatterns = [
    path('index/', views.index),
    path('show/<int:id>/', views.show),
    path('test_get/', views.test_get),
    path('test_post/', views.test_post),
    path('test_render/', views.test_render),
    path('test_templateview/', TestTemplateView.as_view()),
    path('test_listview/', TestListView.as_view()),
]