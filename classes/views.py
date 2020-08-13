from django.shortcuts import render
from .models import Classes
# Create your views here.
def Class_list(request):
    classes = Classes.objects.all().order_by('id')
    return render(request, 'classes/class_list.html', {'classes': classes})