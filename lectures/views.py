from django.shortcuts import render
from .models import Lecture
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
def Lecture_list(request):
    lectures = Lecture.objects.all().order_by('id')
    return render(request, 'lectures/lecture_list.html', {'lectures': lectures})

class LectureCreateView(CreateView):
    model = Lecture
    fields = ['lecture_title', 'lecture_note']  

class LectureUpdateView(UpdateView):
    model = Lecture
    fields = ['lecture_title', 'lecture_note']  

# class AnnoucementDeleteView(LoginRequiredMixin, DeleteView):
#     model = Annoucement
#     success_url = reverse('home.html')
