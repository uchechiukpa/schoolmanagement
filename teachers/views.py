from django.shortcuts import render
from .models import Teacher
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
def Teacher_list(request):
    teachers = Teacher.objects.all().order_by('id')
    return render(request, 'teachers/teachers_list.html', {'teachers': teachers})


class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['firstname', 'lastname','email']  

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['firstname', 'lastname','email']  

# class AnnoucementDeleteView(LoginRequiredMixin, DeleteView):
#     model = Annoucement
#     success_url = reverse('home.html')
