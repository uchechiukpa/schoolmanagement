from django.shortcuts import render
from .models import Course
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse


# Create your views here.
def Course_list(request):
    courses = Course.objects.all().order_by('id')
    return render(request, 'courses/course_list.html', {'courses': courses})

class CourseCreate(CreateView):
    model = Course
    fields = ['course_title', 'course_code']

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['course_title', 'course_code']

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse('courses:course_list')