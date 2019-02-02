from django.shortcuts import render
from .models import Job
# Create your views here.

def home(request):

    jobs = Job.objects   # object from jobs model
    return render(request , 'jobs/home.html' , {'jobs':jobs}) #dictionary off all jobs objects from jobs model
