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



# class Subject(models.Model):

    # subject_name=models.CharField(max_length=255)
    # school_class = model.ChoiceField(choices=YEAR_IN_SCHOOL_CHOICES)


    # def __str__(self):
    #     return self.subject_name

# class Class(models.Model):
#     PRIMARYONE = 'PR 1'
#     PRIMARYTWO = 'PR 2'
#     PRIMARYTHREE = 'PR 3'
#     PRIMARYFOUR = 'PR 4'
#     PRIMARYFIVE = 'PR 5'
#     PRIMARYSIX = 'PR 6'
#     YEAR_IN_SCHOOL_CHOICES = [
#         (PRIMARYONE, 'PRIMARY 1'),
#         (PRIMARYTWO, 'PRIMARY 2'),
#         (PRIMARYTHREE, 'PRIMARY 3'),
#         (PRIMARYFOUR, 'PRIMARY 4'),
#         (PRIMARYFIVE, 'PRIMARY 5'),
#         (PRIMARYSIX, 'PRIMARY 6'),
#     ]
#     student_class = models.CharField(max_length=10, choices=YEAR_IN_SCHOOL_CHOICES, default=PRIMARYONE)
#     subjectforclass = models.ForiegnKey(Subjectmax_length=30, on_delete=DO_NOTHING)

    # class Meta:
    #     verbose_name_plural='classes'

    # def __str__(self):
    #     return self.student_class 


class Student(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    student_id=models.CharField(max_length=255)
  
    def __str__(self):
        return self.admin.username



@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Teacher.objects.create(admin=instance)
        if instance.user_type==3:
             Student.objects.create(admin=instance, student_id="")


@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.teacher.save()
    if instance.user_type==3:
        instance.student.save()

            # print(student_name)

