"""Upd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from app import views
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from app.models import Employee
urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/",views.index),
    path("send/",views.send),
    path("home/",ListView.as_view(template_name="home.html",model=Employee),name="home"),
    path("update<int:pk>/",views.Update.as_view(),name="update"),
    path("delete<int:pk>/",views.Delete.as_view(),name="delete"),
]
