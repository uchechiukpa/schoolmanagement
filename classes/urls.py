from django.urls import path, include
from . import views

app_name = 'classes'

urlpatterns = [
    path('', views.Class_list, name= 'class_list'),
    path('add/', views.ClassesCreateView.as_view(), name='add_classes'),
    path('update/<int:pk>/', views.ClassesUpdateView.as_view(), name='update_classes'),
    path('delete/<int:pk>/', views.ClassesDeleteView.as_view(), name='delete_classes'),
]