from django.db import models
from courses.models import Course

# Create your models here.
class Assignment(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)


    def __str__(self):
        return self.question