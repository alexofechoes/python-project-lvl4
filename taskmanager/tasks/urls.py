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

    path(
        'task-status',
        views.TaskStatusListView.as_view(),
        name='status-list',
    ),
    path(
        'task-status/<int:pk>',
        views.TaskStatusDetailView.as_view(),
        name='status-detail',
    ),
    path(
        'task-status/create',
        views.TaskStatusCreateView.as_view(),
        name='status-create',
    ),
    path(
        'task-status/<int:pk>/edit',
        views.TaskStatusUpdateView.as_view(),
        name='status-edit',
    ),
    path(
        'task-status/<int:pk>/delete',
        views.TaskStatusDeleteView.as_view(),
        name='status-delete',
    ),
]
