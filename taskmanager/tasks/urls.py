"""Tasks URL Configuration."""
from django.urls import path

from taskmanager.tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),
    path('new', views.TaskCreateView.as_view(), name='create'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.TaskUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='delete'),
    path('<int:pk>/progress', views.progress, name='progress'),
    path('<int:pk>/fulfilled', views.fulfilled, name='fulfilled'),
    path('<int:pk>/returned', views.returned, name='returned'),
    path('<int:pk>/canceled', views.canceled, name='canceled'),
]
