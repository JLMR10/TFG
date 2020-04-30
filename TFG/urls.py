"""TFG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from tfgApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^canvasDemo', views.canvasDemo),
    path('signup/', views.signUp, name='signup'),
    path('postsignup/', views.postsignup),
    path('postsign/', views.postsign),
    re_path(r'^$', views.signIn),
    path('logout/', views.logout, name="log"),
]
"""+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"""

