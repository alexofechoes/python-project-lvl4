"""Views for tasks app."""

from django.shortcuts import render


def home(request):
    """Home view."""
    return render(request, 'tasks/home.html')
