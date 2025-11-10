from django.contrib import admin
from .models import LongLeaveRecord, ClassInfo, AbsentStudents


# Register your models here.
admin.site.register(LongLeaveRecord)
admin.site.register(ClassInfo)
admin.site.register(AbsentStudents)
