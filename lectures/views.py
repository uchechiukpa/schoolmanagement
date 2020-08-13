from django.shortcuts import render
from .models import Lecture
# Create your views here.
def Lecture_list(request):
    lectures = Lecture.objects.all().order_by('id')
    return render(request, 'lectures/lecture_list.html', {'lectures': lectures})