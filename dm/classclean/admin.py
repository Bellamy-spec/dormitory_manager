from django.contrib import admin
from .models import ClassCleanRecord, ClassCleanScore, OutLookRecord

# Register your models here.
admin.site.register(ClassCleanRecord)
admin.site.register(ClassCleanScore)
admin.site.register(OutLookRecord)
