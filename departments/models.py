from django.db import models
from teachers.models import Teacher
from django.urls import reverse

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=45)
    dept_head = models.CharField(max_length=45)
    teacher_id = models.ManyToManyField(Teacher)


    def __str__(self):
        return self.dept_name

    def get_absolute_url(self):
        return reverse('departments:dept_list')

