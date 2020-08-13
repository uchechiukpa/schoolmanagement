from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy
from .models import Assigment
from django.contrib.auth.mixins import LoginRequiredMixin


def Assigment_list(request):
    assigments = Assigment.objects.all().order_by('id')
    return render(request, 'assigments/assigment_list.html', {'assigments': assigments})


# class AssignmentCreateView(LoginRequiredMixin, CreateView):
#     model = Assignment
#     fields = ['annoucements_title', 'Annoucements_description']  

# class AssignmentUpdateView(LoginRequiredMixin, UpdateView):
#     model = Assignment
#     fields = ['annoucements_title', 'Annoucements_description']    

# class AssignmentDeleteView(LoginRequiredMixin, DeleteView):
#     model = Assignment
#     # success_url = reverse_lazy('departments:dept_list')
