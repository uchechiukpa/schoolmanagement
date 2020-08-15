from django.urls import path, include
from . import views

app_name = 'submissions'

urlpatterns = [
    path('', views.Submission_list, name= 'submission_list'),
    path('add/', views.SubmissionCreateView.as_view(), name='add_submission'),
    path('update/<int:pk>/', views.SubmissionUpdateView.as_view(), name='update_submission'),

]