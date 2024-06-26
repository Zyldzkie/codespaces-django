"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from main.core import views as core_views
"""path("", core_views.index),

if we have home now
path('', core_views.home , name="home"),
"""
urlpatterns = [
    path('', core_views.home , name="home"),
    path("signin", core_views.signin, name="signin"),
    path("signup", core_views.signup, name="signup"),
    path('signout', core_views.signout, name='signout'),
    path('premium', core_views.become_premium, name='become_premium'),
    path('search', core_views.search, name='search'),
    path('search_results', core_views.search_results, name='search_results'),
    path('about', core_views.about, name='about'),
    path('item/<int:item_id>/', core_views.itemroom, name='itemroom'),
    path('sell/', include('shopitem.urls')),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
