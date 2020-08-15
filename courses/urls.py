from django.urls import path, include
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.Course_list, name= 'course_list'),
    path('add/', views.CourseCreate.as_view(), name= 'add-course'),
    path('update/<int:pk>/', views.CourseUpdateView.as_view(), name='update_course'),
    path('delete/<int:pk>/', views.CourseDeleteView.as_view(), name='delete_course')
]