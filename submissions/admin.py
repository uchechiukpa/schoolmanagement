from django.contrib import admin
from .models import Submission, UploadAssignment,StudentGrade
# Register your models here.

admin.site.register(Submission)
admin.site.register(UploadAssignment)
admin.site.register(StudentGrade)