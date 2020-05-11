"""Models for tasks app."""

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_fsm import FSMField, transition  # type: ignore


class Tag(models.Model):
    name = models.CharField(max_length=120, unique=True) # noqa WPS432

    def __str__(self):
        return '{name}'.format(name=self.name)


class TaskState:
    NEW = 'new' # noqa WPS115
    PROGRESS = 'progress' # noqa WPS115
    RETURNED = 'returned' # noqa WPS115
    FULFILLED = 'fulfilled' # noqa WPS115
    CANCELED = 'canceled' # noqa WPS115


class Task(models.Model):
    title = models.CharField(max_length=120) # noqa WPS432
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='creator',
    )
    assigner = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='assigner',
    )
    state = FSMField(default=TaskState.NEW)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    canceled_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{title} ({id})'.format(title=self.title, id=self.id)

    def tags_to_string(self):
        return ', '.join(tag.name for tag in self.tags.all())

    def get_absolute_url(self):
        return reverse('tasks:detail', args=[self.pk])

    @transition(
        field=state,
        source=[TaskState.NEW, TaskState.RETURNED],
        target=TaskState.PROGRESS,
    )
    def progress(self):
        pass # noqa WPS420

    @transition(
        field=state,
        source=TaskState.PROGRESS,
        target=TaskState.FULFILLED,
    )
    def fulfilled(self):
        pass # noqa WPS420

    @transition(
        field=state,
        source=TaskState.FULFILLED,
        target=TaskState.RETURNED,
    )
    def returned(self):
        pass # noqa WPS420

    @transition(
        field=state,
        source=TaskState.FULFILLED,
        target=TaskState.CANCELED,
    )
    def canceled(self):
        self.canceled_at = datetime.now() # noqa WPS601
