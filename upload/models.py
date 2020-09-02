from django.db import models

# Create your models here.





class AssignmentUpload(models.Model):
    student_name = models.CharField(max_length = 255)
    submitted_assignment = models.FileField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_name

