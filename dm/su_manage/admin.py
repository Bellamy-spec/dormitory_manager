from django.contrib import admin
from .models import SchoolYear, Department, Member, StudentUser


# Register your models here.
admin.site.register(SchoolYear)
admin.site.register(Department)
admin.site.register(Member)
admin.site.register(StudentUser)
