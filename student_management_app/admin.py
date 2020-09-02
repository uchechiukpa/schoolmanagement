from django.contrib import admin
# from .models import Student 

# Register your models here.

from django.contrib.auth.admin import UserAdmin

from student_management_app.models import CustomUser, Student, Teacher
# , Subject



class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel)
admin.site.register(Student)
admin.site.register(Teacher)
