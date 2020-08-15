from django.urls import path, include
from . import views

app_name = 'announcements'

urlpatterns = [
    path('', views.annoucements_list, name="annoucements_list"),
    path('add/', views.AnnoucementCreateView.as_view(), name='add_annoucement'),
    path('update/<int:pk>/', views.AnnoucementUpdateView.as_view(), name='update_annoucement'),
   ]