from django.db import models
from django.db.models.base import Model

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

class Habits(models.Model):
    done_for_today = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    comment = models.TextField()
