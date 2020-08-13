from django.db import models

# Create your models here.
class Annoucement(models.Model):
    annoucement_title = models.CharField(max_length=45)
    annoucement_description = models.CharField(max_length=45)

    def __str__(self):
        return self.annoucements_title   