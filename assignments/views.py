from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy
from .models import Assigment
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course

def Assigment_list(request):
    assigments = Assigment.objects.all().order_by('id')

    # courses = Course.objects.all().order_by('id')

    return render(request, 'assignments/assigment_list.html', {'assigments': assigments})


class AssignmentCreateView(CreateView):
    model = Assigment
    fields = ['questions']  

class AssignmentUpdateView(UpdateView):
    model = Assigment
    fields = ['questions']    

class AssignmentDeleteView(DeleteView):
    model = Assigment
    success_url = reverse_lazy('departments:dept_list')
