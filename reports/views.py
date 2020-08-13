from django.shortcuts import render
from .models import Report
from students.models import Student
# Create your views here.
def Report_list(request):

    reports = Report.objects.all().order_by('id')
    # students = get_object_or_404(Student, pk=student_id)
    students = Student.objects.all()
    context = {
       'reports': reports,
       'students': students 
    }
    return render(request, 'reports/report_list.html', {'context': context})
