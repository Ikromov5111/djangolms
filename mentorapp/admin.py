from django.contrib import admin
from .models import TaskModel
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class MentorAdmin(ImportExportModelAdmin):
    model= TaskModel
    list_display = ['task_name','file','group','dedlayn','username']
admin.site.register(TaskModel,MentorAdmin)