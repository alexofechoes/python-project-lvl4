"""Taskmanager URL Configuration."""

from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path

urlpatterns = [
    path('', include('taskmanager.tasks.urls')),
    path('auth/login', views.LoginView.as_view(), name='login'),
    path('auth/logout', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
