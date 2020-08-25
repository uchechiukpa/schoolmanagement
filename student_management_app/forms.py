from django import forms
# from student_management_app.models import Subject
# from subjects.models import Subject



class AddStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))



    

    YEAR_IN_SCHOOL_CHOICES = [
        ('JSS1', 'JSS 1'),
        ('JSS2', 'JSS 2'),
        ('JSS3', 'JSS 3'),
        ('SSS1', 'SSS 1'),
        ('SSS2', 'SSS 2'),
        ('SSS3', 'SSS 3'),
    ]
    # student_class = models.CharField(max_length=10, choices=YEAR_IN_SCHOOL_CHOICES, default=PRIMARYONE)

    studentclass=forms.ChoiceField(label='Class',choices=YEAR_IN_SCHOOL_CHOICES,widget=forms.Select(attrs={"class":"form-control"}))
    # subjects=Subject.objects.all()
    # subject_list=[]
    # for subject in subjects:
    #     small_subject=(subject.id, subject.subject_name)
    #     subject_list.append(small_subject)

    # subjects=forms.MultipleChoiceField(label='Subject', widget=forms.CheckboxSelectMultiple, choices=subject_list)

