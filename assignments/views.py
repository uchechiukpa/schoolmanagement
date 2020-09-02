from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.
from .models import Assignment



def assignment_list(request):
    assignments = Assignment.objects.all().order_by('id')
    return render(request,'assignments/assignments_list.html', {'assignments': assignments})

class AssignmentCreateView(CreateView):
    model = Assignment
    fields = ['course_id','question','upload_question'] 
    

class AssignmentUpdateView(UpdateView):
    model = Assignment
    fields = ['course_id','question',]    