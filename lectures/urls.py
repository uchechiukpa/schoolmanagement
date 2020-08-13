from django.urls import path, include
from . import views

app_name = 'lectures'

urlpatterns = [
    path('', views.Lecture_list, name= 'lecture_list')
]