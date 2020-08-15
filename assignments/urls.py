from django.urls import path, include
from . import views

app_name = 'assignments'

urlpatterns = [
    path('', views.Assigment_list, name= 'assigment_list'),
    path('add/', views.AssignmentCreateView.as_view(), name='add_assigment'),
    path('update/<int:pk>/', views.AssignmentUpdateView.as_view(), name='update_assigment'),
    path('delete/<int:pk>/', views.AssignmentDeleteView.as_view(), name='delete_assigment')
]