from django.shortcuts import render


def student_home(request):
    return render(request, "students/students_home.html")