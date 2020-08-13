from django.shortcuts import render
from .models import Report
from students.models import Student
# Create your views here.
def Report_list(request):

    
    students = Student.objects.get()
    reports = students.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})
