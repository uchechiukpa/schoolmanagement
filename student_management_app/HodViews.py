from django.contrib import messages 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse 
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddStudentForm,AssignmentForm
from student_management_app.models import CustomUser, Teacher, Student
from announcements.models import Annoucement
from assignments.models import Assignment 
from courses.models import Course
from django.db.models  import Count
from submissions.models import Submission, UploadAssignment
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from upload.models import AssignmentUpload




def admin_home(request):
    return render(request, 'base_layout.html')

def upload_view(request):
    return render(request, 'students/upload_file.html')







def teacher_home(request):
    courses =  Course.objects.all()
    submissions = Submission.objects.all()
    class_id = request.user.student.student_id
    assignments = Assignment.objects.all()
    announcements = Annoucement.objects.all()
    item = len(announcements)


    

    if('JSS1' == request.user.teacher.teacher_class):
        class_name = 'JSS1'
    elif('JSS2' == request.user.teacher.teacher_class):
        class_name = 'JSS2'
    elif('JSS3' == request.user.teacher.teacher_class):
        class_name = 'JSS3'
    elif('SS1' == request.user.teacher.teacher_class):
        class_name = 'SSS1'
    elif('SSS2' == request.user.teacher.teacher_class):
        class_name = 'SSS2'
    else:
        class_name = 'SSS3'


    
    if('JSS1' == request.user.student.student_id):
        classname = 'JSS1'
    elif('JSS2' == request.user.student.student_id):
        classname = 'JSS2'
    elif('JSS3' == request.user.student.student_id):
        classname = 'JSS3'
    elif('SS1' == request.user.student.student_id):
        classname = 'SSS1'
    elif('SSS2' == request.user.student.student_id):
        classname = 'SSS2'
    else:
        classname = 'SSS3'



    context = {
        'courses': courses, 
        'submissions': submissions,
        'assignments': assignments,
        'announcements': announcements,
        'item': item,
        'class_name': class_name,
       
    }
    
    # print(request.user.student.student_id)
    # print(request.user.teacher.teacher_class)
    return render(request, 'teachers/teachers_home.html', context)

    
def add_teacher(request):
    courses =  Course.objects.all()
    
    return render(request, "hod_template/add_teacher_template.html", {'courses': courses})


def add_teacher_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")

    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        StudentsClass=request.POST.get("StudentsClass")
        Address=request.POST.get("Address")
        Gender=request.POST.get("Gender")
        Bio=request.POST.get("Bio")
        Subject=request.POST.get("Subject")
        # try:
        user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
        # print('hi')
        user.teacher.teacher_class=StudentsClass
        user.teacher.address=Address
        user.teacher.gender=Gender
        user.teacher.bio=Bio
        user.teacher.subject=Subject
        user.save()
        messages.success(request,"Successfully Added Teacher")
        return HttpResponseRedirect(reverse("add_teacher"))
        # except:
        #     messages.error(request,"Failed to Add Teacher")
        #     return HttpResponseRedirect(reverse("add_teacher"))   



def add_student(request):
    form=AddStudentForm()
    return render(request, "hod_template/add_student_template.html", {"form": form})


def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddStudentForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            studentclass=form.cleaned_data["studentclass"]
            
            # try: 
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
            user.student.student_id=studentclass
            user.save()
            messages.success(request,"Successfully Added Student")
            return HttpResponseRedirect(reverse("add_student"))
            # except:
            # messages.error(request,"Failed to Add Student")
            # return HttpResponseRedirect(reverse("add_student"))

        else:

            form=AddStudentForm(request.POST)
            return render(request, "hod_template/add_student_template.html", {"form": form})

def student_list(request):
    students = Student.objects.all().order_by('id')
    

    if('JSS1' == request.user.teacher.teacher_class):
        classname = 'JSS1'
    elif('JSS2' == request.user.teacher.teacher_class):
        classname = 'JSS2'
    elif('JSS3' == request.user.teacher.teacher_class):
        classname = 'JSS3'
    elif('SS1' == request.user.teacher.teacher_class):
        classname = 'SSS1'
    elif('SSS2' == request.user.teacher.teacher_class):
        class_name = 'SSS2'
    else:
        classname = 'SSS3'

    return render(request, 'hod_template/student_list.html', {'students': students , 'classname': classname})
 



def show_annocements(request):
    studentsannounces = Annoucement.objects.all()
    students = CustomUser.objects.filter(user_type=3)
    return render(request, 'students/announcements_list.html', {"studentsannounces": studentsannounces})



   
# class StudentSubmit()

