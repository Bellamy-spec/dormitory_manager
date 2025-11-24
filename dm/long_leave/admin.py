from django.contrib import admin
from .models import LongLeaveRecord, ClassInfo, AbsentStudents, StayTask, StayRecord


# Register your models here.
admin.site.register(LongLeaveRecord)
admin.site.register(ClassInfo)
admin.site.register(AbsentStudents)
admin.site.register(StayTask)
admin.site.register(StayRecord)
