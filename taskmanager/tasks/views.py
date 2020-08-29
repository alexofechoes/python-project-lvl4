"""Views for tasks app."""
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django_filters.views import FilterView  # type: ignore

from taskmanager.tasks.filters import TaskFilter
from taskmanager.tasks.models import Task, TaskStatus


class TaskListView(FilterView):
    filterset_class = TaskFilter
    ordering = ('-created_at',)


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    fields = ('name', 'description', 'assigned_to', 'status', 'tags')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.creator = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    fields = ('name', 'description', 'assigned_to', 'status', 'tags')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')


class TaskStatusListView(ListView):
    model = TaskStatus
    ordering = ('id',)


class TaskStatusDetailView(DetailView):
    model = TaskStatus


class TaskStatusCreateView(CreateView):
    model = TaskStatus
    fields = ('name',)


class TaskStatusUpdateView(UpdateView):
    model = TaskStatus
    fields = ('name',)


class TaskStatusDeleteView(DeleteView):
    model = TaskStatus
    success_url = reverse_lazy('tasks:status-list')
