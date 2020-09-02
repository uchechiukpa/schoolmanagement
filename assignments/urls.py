from django.urls import path, include
from . import views

app_name = 'assignments'

urlpatterns = [
    path('', views.assignment_list, name="assignments_list"),
    path('add/', views.AssignmentCreateView.as_view(), name='add_assignments'),
    path('update/<int:pk>/', views.AssignmentUpdateView.as_view(), name='update_assignments'),
   ]