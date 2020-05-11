"""Tasks URL Configuration."""
from django.urls import path

from taskmanager.tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),
    path('task/create', views.TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='detail'),
    path('task/<int:pk>/edit', views.TaskUpdateView.as_view(), name='edit'),
    path('task/<int:pk>/delete', views.TaskDeleteView.as_view(), name='delete'),
    path('task/<int:pk>/progress', views.progress, name='progress'),
    path('task/<int:pk>/fulfilled', views.fulfilled, name='fulfilled'),
    path('task/<int:pk>/returned', views.returned, name='returned'),
    path('task/<int:pk>/canceled', views.canceled, name='canceled'),
]
