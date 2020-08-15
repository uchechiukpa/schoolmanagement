from django.db import models
from django.urls import reverse
# Create your models here.
class Annoucement(models.Model):
    annoucement_title = models.CharField(max_length=45)
    annoucement_description = models.CharField(max_length=45)

    def __str__(self):
        return self.annoucements_title 

    def get_absolute_url(self):
        return reverse('announcements:annoucements_list')