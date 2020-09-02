from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
# from django.urls import reverse
from .models import Annoucement



def annoucements_list(request):
    announces = Annoucement.objects.all().order_by('id')
    return render(request,'announcements/annoucements_list.html', {'announces': announces})



class AnnoucementCreateView(CreateView):
    model = Annoucement
    fields = ['annoucement_title', 'annoucement_description']  

class AnnoucementUpdateView(UpdateView):
    model = Annoucement
    fields = ['annoucement_title', 'annoucement_description']    

# class AnnoucementDeleteView(LoginRequiredMixin, DeleteView):
#     model = Annoucement
#     success_url = reverse('home.html')


