from django.shortcuts import render

# Create your views here.
from .models import Assignment



def assignment_list(request):
    assigments = Assignment.objects.all().order_by('id')
    return render(request,'announcements/annoucements_list.html', {'announces': announces})