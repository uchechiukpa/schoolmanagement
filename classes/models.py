from django.db import models
from teachers.models import Teacher
from django.urls import reverse

# Create your models here.

class Classes(models.Model):
    FIRSTYEAR = '100L'
    SECONDYEAR = '200L'
    THRIDYEAR= '300L'
    FOURTHYEAR = '400L'
    FIFTHYEAR = '500L'
    YEAR_IN_SCHOOL = [
        (FIRSTYEAR, '100L'),
        (SECONDYEAR , '200L'),
        (THRIDYEAR, '300L'),
        (FOURTHYEAR, '400L'),
        (FIFTHYEAR, '500L'),
    ]
    class_name = models.CharField(max_length=45, choices=YEAR_IN_SCHOOL, default=FIRSTYEAR)
    teacher_id = models.ManyToManyField(Teacher)

    class Meta:
        verbose_name_plural = 'classes'

    def __str__(self):
        return self.class_name

        
    def get_absolute_url(self):
        return reverse('classes:class_list')
    