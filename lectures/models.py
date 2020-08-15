from django.db import models
from django.urls import reverse
from teachers.models import Teacher
from courses.models import Course
# Create your models here.

class Lecture(models.Model):
    lecture_title = models.CharField(max_length=45)
    lecture_note = models.CharField(max_length=45)
    course_id  =  models.ManyToManyField(Course)
    teacher_id = models.ForeignKey(Teacher, on_delete = models.CASCADE)

    def __str__(self):
        return self.lecture_title

def get_absolute_url(self):
        return reverse('lectures:lecture_list')