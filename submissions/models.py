from django.db import models
from django.urls import reverse
from assignments.models import Assigment
from students.models import Student
# Create your models here.

class Submission(models.Model):
    date_submitted = models.DateTimeField()
    assigment_id = models.ForeignKey(Assigment, on_delete = models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)

    def __str__(self):
        return self.date_submitted

    def get_absolute_url(self):
        return reverse('submissions:submission_list')