from django.urls import path, include
from . import views

app_name = 'assignments'

urlpatterns = [
    path('', views.Assigment_list, name= 'assigment_list')
]