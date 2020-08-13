from django.urls import path, include
from . import views

app_name = 'announcements'

urlpatterns = [
    path('', views.annoucements_list, name="annoucements_list")
   ]