from django.db import models

# Create your models here.

class ToMeet(models.Model):
    person = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    date_of_meeting = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)