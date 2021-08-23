from typing import Text
from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, ToMeet, Habits
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


def add_todo_list(request):
    form = request.POST
    text = form['todo_text']
    todo = ToDo(text=text)
    todo.save()
    return redirect(homepage)


def add_for_meeting(request):
    form = request.POST
    data = ToMeet(person=form['data_text'], phone_number=form['data_tel'])
    data.save()
    return redirect(meeting)


def habits(request):
    habit = Habits.objects.all()
    context = {'habit': habit}
    return render(request, 'habits.html', context)


def add_habit(request):
    form = request.POST
    data = Habits(comment=form['comment'], important=form['important'])
    data.save()
    return redirect(habits)