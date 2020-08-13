from django.shortcuts import render
from .models import Student
# Create your views here.
def Students_list(request):
    students = Student.objects.all().order_by('id')
    return render(request, 'students/students_list.html', {'students': students})

