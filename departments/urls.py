from django.urls import path, include
from . import views

app_name = 'departments'

urlpatterns = [
    path('', views.DepartmentView, name= 'dept_list')
]