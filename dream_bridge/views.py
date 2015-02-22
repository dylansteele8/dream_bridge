from django.shortcuts import render
from dream_bridge.apps.users.models import Applicant, Company, Job


# Create your views here.

def home(request):
    data = {}
    return render(request, 'index.html', data)

def applicants(request):
    applicants = Applicant.objects.all()
    data = {'applicants': applicants}
    return render(request, 'applicants.html', data)

def jobs(request):
    jobs = Job.objects.all()
    data = {'jobs': jobs}
    # for job in jobs:
    #     desc_html = job.description
    return render(request, 'jobs.html', data)

def login(request):
    data = {}
    return render(request, 'login.html', data)

def sign_up(request):
    data = {}
    return render(request, 'sign_up.html', data)