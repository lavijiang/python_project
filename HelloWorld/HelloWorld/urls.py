from django.urls import include, re_path,path
 
from . import views,search,search2

urlpatterns = [
    re_path(r'^$', views.hello),
    path('runoob/', views.runoob),
    path('runoob2/', views.runoob2),
    path('search/', search.search),
    path('search-form/', search.search_form),
    path('search-post/', search2.search_post),
]