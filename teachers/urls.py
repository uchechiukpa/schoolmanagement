from . import views
from django.urls import path, include
app_name = 'teachers'

urlpatterns = [
    path('', views.Teacher_list, name= 'teachers_list'),
    path('add/', views.TeacherCreateView.as_view(), name='add_teacher'),
    path('update/<int:pk>/', views.TeacherUpdateView.as_view(), name='update_teacher'),
]