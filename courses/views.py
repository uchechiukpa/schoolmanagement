from django.shortcuts import render
from .models import Course
# Create your views here.
def Course_list(request):
    courses = Course.objects.all().order_by('id')
    return render(request, 'courses/course_list.html', {'courses': courses})