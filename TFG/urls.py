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
    re_path(r'demoChat/(?P<gameId>.*)$', views.demoChat, name='demoChat'),
    path('signUp/', views.signUp, name='signUp'),
    re_path(r'^$', views.signIn, name='signIn'),
    path('logout/', views.logout, name="log"),
    path('mainMenu/', views.mainMenu, name='mainMenu'),
    path('myMaps/', views.myMaps, name='myMaps'),
    path('myMaps/editMap/', views.editMap, name='editMap'),
    path('myMaps/editMap/saveMap/', views.saveMap, name='saveMap'),
    path('myMaps/editMap/saveFromVersion/', views.saveFromVersion, name='saveFromVersion'),
    path('myMaps/editMap/changeVersion/', views.changeVersion, name='changeVersion'),
    path('mainMenu/createGame/', views.createGame, name='createGame'),
    re_path(r'^game/(?P<gameId>.*)$', views.gameView, name='gameView'),
    path('mainMenu/joinGame/', views.joinGame, name='joinGame'),
    path('mainMenu/joinGamePost/', views.joinGamePost, name='joinGamePost'),
    path('mainMenu/joinGameModal/', views.joinGameModal, name='joinGameModal'),
    path('mainMenu/JoinGameCharacterModal/', views.joinCharacterModal, name='joinCharacterModal'),
    path('mainMenu/editProfile/', views.editProfile, name='editProfile'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    ##re_path(r'createGame/(?P<gameId>.*)$', views.createGame, name='createGame'),

    ##re_path(r'^myMaps/(?P<map>\w+)/$', views.editMap, name='editMap')
]
"""+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"""

