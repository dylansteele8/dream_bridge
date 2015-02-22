from django.shortcuts import render
from dream_bridge.apps.users.models import UserD, UserDVideo, Company, Job


# Create your views here.

def home(request):
    users = UserD.objects.all()
    data = {'users': users}
    return render(request, 'index.html', data)

def login(request):
    data = {}
    return render(request, 'login.html', data)

def sign_up(request):
    data = {}
    return render(request, 'sign_up.html', data)