from django.urls import path, include
from . import views

app_name = 'submissions'

urlpatterns = [
    path('', views.Submission_list, name= 'submission_list')
]