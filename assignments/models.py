from django.db import models
from courses.models import Course

# Create your models here.
class Assigment(models.Model):
    course_id  =  models.ManyToManyField(Course)
    questions = models.CharField(max_length=45)

    def __str__(self):
        return self.questions