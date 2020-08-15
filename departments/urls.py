from django.urls import path, include
from . import views

app_name = 'departments'

urlpatterns = [
    path('', views.DepartmentView, name= 'dept_list'),
    path('add/', views.DepartmentCreateView.as_view(), name='add_department'),
    path('update/<int:pk>/', views.DepartmentUpdateView.as_view(), name='update_department'),
    path('delete/<int:pk>/', views.DepartmentDeleteView.as_view(), name='delete_department')
]