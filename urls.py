"""
URL configuration for sheridan project.

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
from education.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('about/',about),
    path('courses/',courses), 
    path('camp/',camp),
    path('degree/',degree),
    path('labs/',labs),
    path('programs/',programs),
    

    
    path('accesbility/',accesbility),
    path('alumni/',alumni),
    path('extra/',extra),
    path('apply/',apply, name='apply'),
    path('apply1/',apply1, name='apply1'),
    path('apply2/',apply2, name='apply2'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('log/',log),
    path('subs/',subs,name='subs'),
    
]

