from django.contrib import admin

from taskmanager.tasks.models import Tag, Task, TaskStatus

admin.site.register(Tag)
admin.site.register(TaskStatus)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'assigned_to',
        'creator',
        'status',
        'created_at',
        'tags_to_string',
    )

    readonly_fields = (
        'creator',
        'created_at',
    )

    def save_model(self, request, task, form, change):
        task.creator = request.user
        task.save()
