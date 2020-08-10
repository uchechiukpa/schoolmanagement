from django import forms
from .models import Teacher , Student

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('firstname', 'lastname','email')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('firstname', 'lastname', 'email', 'courses')