from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic/',include('apps.basic.urls')),
    path('users/',include('apps.users.urls')),
    re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    re_path('static/(?P<path>.*)', serve, {"document_root": settings.STATIC_ROOT}),
    path('api-token-auth/', obtain_auth_token),
    path('api-jwt-token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('docs/', include_docs_urls('我的商城接口')),
]