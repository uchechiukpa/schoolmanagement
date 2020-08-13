from django.shortcuts import render
from .models import Department

# Create your views here.
def DepartmentView(request):
    depts = Department.objects.all().order_by('id')
    return render(request, 'department/dept_list.html', {'depts': depts})