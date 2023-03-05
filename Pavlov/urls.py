"""Pavlov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from .views import home

urlpatterns = [
    path('', home, name='home'),

    path('admin/', admin.site.urls),
    
    # api endpoints
    path('api/auth/', include('access.api.v1.urls')),
    path('api/bot/', include('bot.api.v1.urls')),
    path('api/commands/', include('command.api.v1.urls')),
    path('api/schedule/', include('schedule.api.v1.urls')),
    path('api/user/', include('user.api.v1.urls')),
]
