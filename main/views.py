from django.shortcuts import render, HttpResponse
from .models import ToDo, ToMeet

# Create your views here.

def homepage(request):
    todo_list = ToDo.objects.all()
    return render(request, 'index.html', {'todo_list': todo_list})

def test(request):
    return render(request, 'test.html')

def meeting(request):
    meet = ToMeet.objects.all()
    return render(request, 'meeting.html', {'tomeet': meet})

