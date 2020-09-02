from django import forms
from courses.models import Course
from student_management_app.models import Student,Teacher
from assignments.models import Assignment
from submissions.models import UploadAssignment, StudentGrade
from upload.models import AssignmentUpload
 





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



class AssignmentForm(forms.Form):
   
    student_name = forms.CharField(max_length=255)
    submitted_assignment = forms.FileField()


class UploadAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('course_id','question','upload_question')
    
class StudentGradeForm(forms.Form):
    courses = Course.objects.all()
    students = Student.objects.all()
    teachers = Teacher.objects.all()

    course_details=[]
    for teacher in teachers:
        for student in students:
            if student.student_id == teacher.teacher_class:
                small_course=(student.admin.first_name + " " + student.admin.last_name, student.admin.first_name + " " + student.admin.last_name)
                course_details.append(small_course)

    # print(course_details)
    student=forms.ChoiceField(label='Student Name', choices=course_details, widget=forms.Select(attrs={"class":"form-control"}))
    test=forms.DecimalField(label='Text Score', widget=forms.NumberInput(attrs={"class":"form-control"}))
    exam=forms.DecimalField(label='Exam Score', widget=forms.NumberInput(attrs={"class":"form-control"}))
    percentage=forms.DecimalField(label='Overall Score',widget=forms.NumberInput(attrs={"class":"form-control"}))



      