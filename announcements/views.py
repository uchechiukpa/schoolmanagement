from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse
from .models import Annoucement
from django.contrib.auth.mixins import LoginRequiredMixin


def annoucements_list(request):
    announces = Annoucement.objects.all().order_by('id')
    return render(request,'announcement/announcement.html', {'announces': announces})

# class AnnoucementCreateView(LoginRequiredMixin, CreateView):
#     model = Annoucement
#     fields = ['annoucements_title', 'Annoucements_description']  

# class AnnoucementUpdateView(LoginRequiredMixin, UpdateView):
#     model = Annoucement
#     fields = ['annoucements_title', 'Annoucements_description']    

# class AnnoucementDeleteView(LoginRequiredMixin, DeleteView):
#     model = Annoucement
#     success_url = reverse('home.html')


