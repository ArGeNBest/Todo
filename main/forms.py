from django.db.models import fields
from django.forms import ModelForm
from .models import ToDo

class TodoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'
