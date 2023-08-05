from django.contrib import admin
from .models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "complete", "created")
    list_filter = ("user", "complete")
