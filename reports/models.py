from django.db import models
from students.models import Student

# Create your models here.
class Report(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)

    def __str__(self):
        return self.student_id