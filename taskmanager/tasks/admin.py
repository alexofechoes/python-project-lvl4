from django.contrib import admin

from taskmanager.tasks.models import Tag, Task

admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'assigner',
        'creator',
        'state',
        'created_at',
        'updated_at',
        'canceled_at',
        'tags_to_string',
    )

    readonly_fields = (
        'state',
        'creator',
        'created_at',
        'updated_at',
        'canceled_at',
    )

    def save_model(self, request, task, form, change):
        task.creator = request.user
        task.save()
