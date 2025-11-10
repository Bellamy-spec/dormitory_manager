from django.contrib import admin
from .models import DateRecord, ClassRecord, LateStudent


# Register your models here.
admin.site.register(DateRecord)
admin.site.register(ClassRecord)
admin.site.register(LateStudent)
