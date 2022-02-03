"""NoUgly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from NoUgly import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('rest-auth/', include('rest_auth.urls')), # 로그인, 로그아웃, 비밀번호 재설정 및 비밀번호 변경과 같은 기본 인증 기능이 있습니다.
    path('rest-auth/registration/', include('rest_auth.registration.urls')),  # 등록 및 소셜 미디어 인증과 관련된 논리가 있습니다.

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)