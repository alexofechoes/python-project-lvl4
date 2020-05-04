"""Tasks URL Configuration."""
from django.urls import path

from taskmanager.tasks import views

urlpatterns = [
    path('', views.home),
]
