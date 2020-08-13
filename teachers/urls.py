from . import views
from django.urls import path, include
app_name = 'teachers'

urlpatterns = [
    path('', views.Teacher_list, name= 'teachers_list')
]