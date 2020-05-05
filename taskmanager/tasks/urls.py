"""Tasks URL Configuration."""
from django.urls import path

from taskmanager.tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.home, name='index'),
]
