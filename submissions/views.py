from django.shortcuts import render
from .models import Submission
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
def Submission_list(request):
    submissions = Submission.objects.all().order_by('id')
    return render(request, 'submissions/submission_list.html', {'submissions': submissions})


class SubmissionCreateView(CreateView):
    model = Submission
    fields = ['date_submitted']  

class SubmissionUpdateView(UpdateView):
    model = Submission
    fields = ['date_submitted']  

# class AnnoucementDeleteView(LoginRequiredMixin, DeleteView):
#     model = Annoucement
#     success_url = reverse('home.html')
