from django.contrib import admin
from .models import Program, Performer, Costume, Designer


# Register your models here.
admin.site.register(Program)
admin.site.register(Performer)
admin.site.register(Costume)
admin.site.register(Designer)
