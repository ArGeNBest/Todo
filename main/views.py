from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, ToMeet
from .forms import TodoForm
# Create your views here.

def homepage(request):
    todo_list = ToDo.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'index.html', context)

def test(request):
    return render(request, 'test.html')

def meeting(request):
    meet = ToMeet.objects.all()
    return render(request, 'meeting.html', {'tomeet': meet})


def add_todo(request):
    form = TodoForm()
    form = TodoForm(request.POST)
    if form.is_valid():
        form.save()
    context = {'todo_list': form}
    return redirect(homepage)
