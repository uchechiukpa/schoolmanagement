# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Student(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    courses = models.CharField(max_length=45)

    def __str__(self):
        return self.firstname + ' ' + self.lastname



class Teacher(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)


    def __str__(self):
        return self.firstname + ' ' + self.lastname


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
