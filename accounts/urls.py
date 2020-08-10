from django.urls import path
from .views import update_profile

urlpatterns = [
    path('home/', update_profile, name='home')

]