from django.shortcuts import render
from .models import Submission
# Create your views here.
def Submission_list(request):
    submissions = Submission.objects.all().order_by('id')
    return render(request, 'submission/submission_list.html', {'submissions': submissions})
