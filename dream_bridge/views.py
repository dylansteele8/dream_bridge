from django.shortcuts import render

# Create your views here.

def home(request):
    data = {}
    return render(request, 'index.html', data)

def login(request):
    data = {}
    return render(request, 'login.html', data)

def sign_up(request):
    data = {}
    return render(request, 'sign_up.html', data)