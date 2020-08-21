from django.db import models

# Create your models here.
class Class(models.Model):
    PRIMARYONE = 'PR 1'
    PRIMARYTWO = 'PR 2'
    PRIMARYTHREE = 'PR 3'
    PRIMARYFOUR = 'PR 4'
    PRIMARYFIVE = 'PR 5'
    PRIMARYSIX = 'PR 6'
    YEAR_IN_SCHOOL_CHOICES = [
        (PRIMARYONE, 'PRIMARY 1'),
        (PRIMARYTWO, 'PRIMARY 2'),
        (PRIMARYTHREE, 'PRIMARY 3'),
        (PRIMARYFOUR, 'PRIMARY 4'),
        (PRIMARYFIVE, 'PRIMARY 5'),
        (PRIMARYSIX, 'PRIMARY 6'),
    ]
    student_class = models.CharField(max_length=10, choices=YEAR_IN_SCHOOL_CHOICES, default=PRIMARYONE)

    class Meta:
        verbose_name_plural='classes'

    def __str__(self):
        return self.student_class 