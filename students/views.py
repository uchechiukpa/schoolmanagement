from django.shortcuts import render
from .models import Student
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
def Students_list(request):
    students = Student.objects.all().order_by('id')
    return render(request, 'students/students_list.html', {'students': students})

class StudentCreateView(CreateView):
    model = Student
    fields = ['firstname', 'lastname','email','courses']  

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['firstname', 'lastname','email','courses']  

# class AnnoucementDeleteView(LoginRequiredMixin, DeleteView):
#     model = Annoucement
#     success_url = reverse('home.html')

