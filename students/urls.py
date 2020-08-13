from . import views
from django.urls import path, include
app_name = 'students'

urlpatterns = [
    path('', views.Students_list, name= 'students_list')
]