from django.shortcuts import render


def teacher_home(request):
    return render(request, "teachers/teacher_home.html")