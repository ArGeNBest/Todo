from django.contrib import admin
from .models import ToMeet, ToDo, Habits

# Register your models here.
admin.site.register(ToMeet)
admin.site.register(ToDo)
admin.site.register(Habits)
