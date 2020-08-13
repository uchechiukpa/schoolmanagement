from django.urls import path, include
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.Course_list, name= 'course_list')
]