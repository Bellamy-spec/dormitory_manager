from django.contrib import admin
from .models import Task, Class, Student


# Register your models here.
admin.site.register(Task)
admin.site.register(Class)
admin.site.register(Student)
