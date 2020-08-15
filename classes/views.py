from django.shortcuts import render
from .models import Classes
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def Class_list(request):
    classes = Classes.objects.all().order_by('id')
    return render(request, 'classes/class_list.html', {'classes': classes})

class ClassesCreateView(CreateView):
    model = Classes
    fields = ['class_name']  

class ClassesUpdateView(UpdateView):
    model = Classes
    fields = ['class_name']  

class ClassesDeleteView(DeleteView):
    model = Classes