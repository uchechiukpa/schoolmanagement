from django.db import models

# Create your models here.



class Subject(models.Model):
    subject_name=models.CharField(max_length=255)
    