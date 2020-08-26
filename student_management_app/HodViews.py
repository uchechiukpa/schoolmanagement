from django.contrib import messages 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddStudentForm
from student_management_app.models import CustomUser, Teacher, Student
from announcements.models import Annoucement
from assignments.models import Assignment 
from courses.models import Course
from django.db.models  import Count
from submissions.models import Submission
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# ,Subject
# from subjects.models import Subject



def admin_home(request):
    return render(request, 'base_layout.html')


def student_home(request):
    courses =  Course.objects.all()
    submissions = Submission.objects.all()
    class_id = request.user.student.student_id
    # class_name = 
    assignments = Assignment.objects.all()
    announcements = Annoucement.objects.all()
    item = len(announcements)


    mention = Course.objects.all()

    if('JSS1' == request.user.student.student_id):
        class_name = 'JSS1'
    elif('JSS2' == request.user.student.student_id):
        class_name = 'JSS2'
    elif('JSS3' == request.user.student.student_id):
        class_name = 'JSS3'
    elif('SS1' == request.user.student.student_id):
        class_name = 'SSS1'
    elif('SSS2' == request.user.student.student_id):
        class_name = 'SSS2'
    else:
        class_name = 'SSS3'


    print(class_name)
    context = {
        'courses': courses, 
        'submissions': submissions,
        'assignments': assignments,
        'announcements': announcements,
        'item': item,
        'class_name': class_name,
    }



    return render(request, 'students/students_home.html', context)
    

def add_teacher(request):
    return render(request, "hod_template/add_teacher_template.html")


def add_teacher_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")

    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        # try:
        user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
        # print('hi')
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
            
            try: 
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
                user.student.student_id=studentclass
                user.save()
                messages.success(request,"Successfully Added Student")
            except:
                    messages.error(request,"Failed to Add Student")
                    return HttpResponseRedirect(reverse("add_student"))

        else:

            form=AddStudentForm(request.POST)
            return render(request, "hod_template/add_student_template.html", {"form": form})

def student_list(request):
    students = Student.objects.all().order_by('id')
    return render(request, 'hod_template/student_list.html', {'students': students})


def show_annocements(request):
    studentsannounces = Annoucement.objects.all()
    students = CustomUser.objects.filter(user_type=3)
    return render(request, 'students/announcements_list.html', {"studentsannounces": studentsannounces})

def show_assignments(request,slug):
    assignments = Assignment.objects.all()
    courses =  Course.objects.all()
    coursedetails = Course.objects.filter(course_name=slug)
    slug = slug 
    # print(assignments)

    context = {
        'assignments': assignments,
        'courses':courses,
        'coursedetails': coursedetails,
        'slug': slug
    }

  
    return render(request, 'students/assignments_list.html', context)

def show_submissions(request, slug):
    assignments = Assignment.objects.all()
    courses =  Course.objects.all()
    submissions = Submission.objects.all()
    coursedetails = Course.objects.filter(course_name=slug)
    # print(coursedetails)

    context = {
        'assignments': assignments,
        "courses": courses,
        'submissions': submissions,
        'coursedetails': coursedetails,

    }

    return render(request, 'students/submissions_list.html', context)

# def assignment_upload(request):
#     if request.method == 'POST' and request.FILES['myfiles']:
#         myfile = request.FILES['myfiles']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'students/upload_file.html', {'uploaded_file_url': uploaded_file_url})
#     return render(request, 'students/upload_file.html')


