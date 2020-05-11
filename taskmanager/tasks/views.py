"""Views for tasks app."""

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from taskmanager.tasks.models import Task


class TaskListView(ListView):
    model = Task
    ordering = ('-created_at')


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    fields = ('title', 'description', 'assigner', 'tags')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.creator = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    fields = ('title', 'description', 'assigner', 'tags')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')


def progress(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.progress()
    task.save()
    return redirect(task)


def fulfilled(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.fulfilled()
    task.save()
    return redirect(task)


def returned(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.returned()
    task.save()
    return redirect(task)


def canceled(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.canceled()
    task.save()
    return redirect(task)
