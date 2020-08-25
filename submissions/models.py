from django.db import models

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