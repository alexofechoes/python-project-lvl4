"""Tasks URL Configuration."""
from taskmanager.tasks.views import TaskStatusListView
from django.urls import path
from django.urls.conf import include

from taskmanager.tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),

    path('tasks/', include([
        path('', views.TaskListView.as_view(), name='index'),
        path('create/', views.TaskCreateView.as_view(), name='create'),
        path('<int:pk>/', include([
            path('', views.TaskDetailView.as_view(), name='detail'),
            path('edit/', views.TaskUpdateView.as_view(), name='edit'),
            path('delete/', views.TaskDeleteView.as_view(), name='delete'),
        ])),
    ])),

    path('task-status/', include([
        path('', views.TaskStatusListView.as_view(), name='status-list'),
        path(
            'create/',
            views.TaskStatusCreateView.as_view(),
            name='status-create',
        ),
        path('<int:pk>/', include([
            path(
                '',
                views.TaskStatusDetailView.as_view(),
                name='status-detail',
            ),
            path(
                'edit/',
                views.TaskStatusUpdateView.as_view(),
                name='status-edit',
            ),
            path(
                'delete/',
                views.TaskStatusDeleteView.as_view(),
                name='status-delete',
            ),
        ])),
    ])),
]
