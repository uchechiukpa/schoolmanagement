from django.db import models
# from django.db.models.fields import models 

# Create your models here.
from assignments.models import Assignment
from courses.models import Course


# Create your models here.
class Submission(models.Model):
    date_submitted = models.DateTimeField()
    assignment_id = models.ForeignKey(Assignment, on_delete=(models.CASCADE))
    subjectcourse = models.ForeignKey(Course, on_delete=(models.CASCADE))
    

    def __str__(self):
        return str(self.date_submitted)

class UploadAssignment(models.Model):
    subject = models.CharField(max_length=255)
    assignment = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    submit_assignment = models.FileField()

    def __str__(self):
        return self.subject +' '+ self.assignment



class StudentGrade(models.Model):
    student_name = models.CharField(max_length=255, default='justin')
    test = models.DecimalField(default=1 ,max_digits=8, decimal_places=1 )
    Exam = models.DecimalField(default=10, max_digits=8, decimal_places=1)
    percentage= models.DecimalField(default=20.9, max_digits=8, decimal_places=1)

    def __str__(self):
        return self.student_name

    