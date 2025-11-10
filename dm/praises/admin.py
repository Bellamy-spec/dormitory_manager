from django.contrib import admin
from .models import Task, ClassSubmit, StudentSubmit


# Register your models here.
admin.site.register(Task)
admin.site.register(ClassSubmit)
admin.site.register(StudentSubmit)
