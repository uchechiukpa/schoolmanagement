from django import forms
from subjects.models import Subject



class AddStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50)
    password=forms.CharField(label="Password",max_length=50)
    username=forms.CharField(label="Username",max_length=50)
    first_name=forms.CharField(label="First Name",max_length=50)
    last_name=forms.CharField(label="Last Name",max_length=50)

