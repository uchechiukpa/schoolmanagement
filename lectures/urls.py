from django.urls import path, include
from . import views

app_name = 'lectures'

urlpatterns = [
    path('', views.Lecture_list, name= 'lecture_list'),
    path('add/', views.LectureCreateView.as_view(), name='add_lecture'),
    path('update/<int:pk>/', views.LectureUpdateView.as_view(), name='update_lecture'),

]