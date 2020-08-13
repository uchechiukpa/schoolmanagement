from django.shortcuts import render
from .models import Teacher
# Create your views here.
def Teacher_list(request):
    teachers = Teacher.objects.all().order_by('id')
    return render(request, 'teachers/teachers_list.html', {'teachers': teachers})
