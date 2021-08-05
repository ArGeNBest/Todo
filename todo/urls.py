"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from main.views import homepage, test
from django.contrib import admin
from django.urls import path
from homework.views import mysite, site



urlpatterns = [
    path('admin/', admin.site.urls),
    path("site", homepage, name='home'),
    path('test/', test, name='test'),
    path('first/', mysite, name='site'),
    path('', site, name='site')
    
]
