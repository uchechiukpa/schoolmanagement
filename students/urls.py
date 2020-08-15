from . import views
from django.urls import path, include
app_name = 'students'

urlpatterns = [
    path('', views.Students_list, name= 'students_list'),
    path('add/', views.StudentCreateView.as_view(), name='add_student'),
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student'),
]