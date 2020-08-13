from django.urls import path, include
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.Report_list, name= 'report_list')
]