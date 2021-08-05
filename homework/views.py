from django.shortcuts import render, HttpResponse

# Create your views here.

def mysite(request):
    return render(request, 'mysite.html')

def site(request):
    return HttpResponse('добро пожаловать в приложение ToDo - Admin')