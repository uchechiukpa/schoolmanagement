from django.db import models

# Create your models here.
class Course(models.Model):
    CLASSES = [
        ('JSS1', 'JSS 1'),
        ('JSS2', 'JSS 2'),
        ('JSS3', 'JSS 3'),
        ('SSS1', 'SSS 1'),
        ('SSS2', 'SSS 2'),
        ('SSS3', 'SSS 3'),
    ]
    course_name=models.CharField(max_length=255)
    course_class=models.CharField(max_length=255, choices=CLASSES, default='JSS1')


    def __str__(self):
        return self.course_name + ' ' + self.course_class