from django.contrib import admin
from .models import TaskModel, CounterHistory

@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('value',)
    
@admin.register(CounterHistory)
class TaskHistoryModelAdmin(admin.ModelAdmin):
    list_display = ('history', 'date')