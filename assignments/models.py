from django.db import models
from courses.models import Course
from django.urls import reverse

# Create your models here.
class Assigment(models.Model):
    course_id  =  models.ManyToManyField(Course)
    questions = models.CharField(max_length=45)

    def __str__(self):
        return self.questions
    
    def get_absolute_url(self):
        return reverse('assignments:assigment_list')
