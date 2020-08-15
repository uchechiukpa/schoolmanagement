from django.shortcuts import render
from .models import Department
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def DepartmentView(request):
    depts = Department.objects.all().order_by('id')
    return render(request, 'departments/dept_list.html', {'depts': depts})

class DepartmentCreateView(CreateView):
    model = Department
    fields = ['dept_name', 'dept_head']

class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['dept_name', 'dept_head']

class DepartmentDeleteView(DeleteView):
    model = Department
    
                  
