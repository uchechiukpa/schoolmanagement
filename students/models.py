from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    courses = models.CharField(max_length=45)

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    def get_absolute_url(self):
        return reverse('students:students_list')