from django.contrib import admin
from .models import Task, WorkloadRecord, SubLesson


# Register your models here.
admin.site.register(Task)
admin.site.register(WorkloadRecord)
admin.site.register(SubLesson)
