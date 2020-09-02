from django.db import models
from courses.models import Course

# Create your models here.
class Assignment(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.TextField(max_length=255,null=True, blank=True)
    upload_question = models.FileField(null=True, blank=True)


    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('assignments:assignments_list')