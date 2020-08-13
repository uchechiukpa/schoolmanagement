from django.db import models
from teachers.models import Teacher

# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length=45)
    course_code = models.IntegerField()
    teacher_id = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.course_title
