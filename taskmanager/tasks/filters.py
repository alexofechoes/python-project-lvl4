import django_filters  # type: ignore
from django.contrib.auth import get_user_model
from django.forms.widgets import CheckboxInput

from taskmanager.tasks.models import Tag, Task, TaskStatus

User = get_user_model()


class TaskFilter(django_filters.FilterSet):
    assigned_to = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    tags = django_filters.ModelChoiceFilter(queryset=Tag.objects.all())
    status = django_filters.ModelChoiceFilter(
        queryset=TaskStatus.objects.all(),
    )
    my_task = django_filters.BooleanFilter(
        method='my_tasks',
        label='My tasks',
        widget=CheckboxInput,
    )

    class Meta:
        model = Task
        fields = ['tags', 'status', 'assigned_to', 'my_task']

    def my_tasks(self, queryset, name, value):  # noqa WPS110
        if self.request is None:
            return queryset

        if value:
            return queryset.filter(
                assigned_to__username=self.request.user.username,
            )

        return queryset
