from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Teacher"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)



class Teacher(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    teacher_class=models.CharField(max_length=255, default='JSS1')
    address=models.TextField(default='5th Adejumo street')
    gender=models.CharField(max_length=255, default='Female')
    subject=models.CharField(max_length=255, default='Maths')
    bio=models.TextField(default='i love to study and read', null = True, blank = True)


    def __str__(self):
        return self.admin.username


class Student(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    student_id=models.CharField(max_length=255)
    address= models.TextField(default='5th Adejumo street')
    gender = models.CharField(max_length=255, default='Female')
    bio = models.TextField(default='i love to study and read')
    
  
    def __str__(self):
        return self.admin.username



@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Teacher.objects.create(admin=instance, teacher_class="", address="", gender="", subject="", bio="")
        if instance.user_type==3:
            Student.objects.create(admin=instance, student_id="", address="", gender="", bio="")


@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.teacher.save()
    if instance.user_type==3:
        instance.student.save()



