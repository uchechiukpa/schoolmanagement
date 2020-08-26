from django.shortcuts import render
from assignments.models import Assignment 
from courses.models import Course

def student_home(request):
    return render(request, "students/students_home.html")


def student_profile(request):
    return render(request, "professor_profile.html")

def student_dashboard(request):
    return render(request, "students/student_dashboard.html")