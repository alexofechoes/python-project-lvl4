"""Models for tasks app."""
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=120, unique=True) # noqa WPS432

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        ordering = ['name']


class TaskStatus(models.Model):
    name = models.CharField(max_length=120, unique=True) # noqa WPS432

    def __str__(self):
        return '{name}'.format(name=self.name)

    def get_absolute_url(self):
        return reverse('tasks:status-detail', args=[self.pk])


class Task(models.Model):
    name = models.CharField(max_length=120) # noqa WPS432
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(TaskStatus, default=1, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='creator',
    )
    assigned_to = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='assigned_to',
    )
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return '{name} ({id})'.format(name=self.name, id=self.id)

    def tags_to_string(self):
        return ', '.join(tag.name for tag in self.tags.all())

    def get_absolute_url(self):
        return reverse('tasks:detail', args=[self.pk])
