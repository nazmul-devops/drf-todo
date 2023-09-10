from django.contrib import admin
from taskManagement.models.models import *


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "project_manager"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "status", "created_by", "project"]


# admin.site.register([ProjectAdmin, TaskAdmin])
