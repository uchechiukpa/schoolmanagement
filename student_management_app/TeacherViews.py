from django.contrib import messages 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddStudentForm, UploadAssignmentForm, StudentGradeForm
from student_management_app.models import CustomUser, Teacher, Student
from announcements.models import Annoucement
from assignments.models import Assignment 
from courses.models import Course
from django.db.models  import Count
from submissions.models import Submission, UploadAssignment, StudentGrade
from django.conf import settings


def teacher_home(request):
    announcements = Annoucement.objects.all()
    item = len(announcements)
    print(item)
    return render(request, "teachers/teachers_home.html", {"item": item, "announcements":announcements})


def annoucements_list(request):
    announcements = Annoucement.objects.all()
    item = len(announcements)
    announces = Annoucement.objects.all().order_by('id')
    return render(request,'teachers/announcements_list.html', {'announces': announces, 'item':item,"announcements":announcements})

def teacher_upload(request):
    announcements = Annoucement.objects.all()
    item = len(announcements)
    if request.method == 'POST':
        form=UploadAssignmentForm(request.POST, request.FILES, {"item": item})

        if form.is_valid():
            form.save()

            messages.success(request,"Assignment Uploaded")
    else:
        form = UploadAssignmentForm()
    return render(request, "assignments/assignment_form.html")


def grade_students(request):
    announcements = Annoucement.objects.all()
    item = len(announcements)
    students = Student.objects.all()
    return render(request, "teachers/students_grade.html", {'students': students, 'item':item})

class StudentGradeCreateView(CreateView):
    model = StudentGrade
    fields = ['test', 'Exam', 'percentage']

def GradeStudentView(request):
    announcements = Annoucement.objects.all()
    item = len(announcements)
    if request.method == "POST":
        form = StudentGradeForm(request.POST)
        if form.is_valid():
            # gradestudent=
            student=form.cleaned_data["student"]
            test=form.cleaned_data["test"]
            exam=form.cleaned_data["exam"]
            percentage=form.cleaned_data["percentage"]
            try:
                studentGrade = StudentGrade(student_name=student, test=test, Exam=exam, percentage=percentage)

                studentGrade.save()
                messages.success(request, 'Graded Student')
                return HttpResponseRedirect(reverse("grade_students"))
            except:
                messages.success(request, 'Not Graded Student')
                return HttpResponseRedirect(reverse("grade_students"))
    else: 
        form = StudentGradeForm()
    return render(request, 'teachers/studentgrade_form.html', {"form": form, 'item': item})

def studentgradeList(request):
    students= Student.objects.all()
    studentgrades = StudentGrade.objects.all()
    gradedstudents=[]
    for studentgrade in studentgrades:
        for student in students:

            if studentgrade.student_name == student.admin.first_name + " " + student.admin.last_name:
                gradedstudents.append(studentgrade)
    
    # print(gradedstudents)
    return render(request, "teachers/gradelist.html", {"gradedstudents": gradedstudents})







def add_submit_assignment(request):

    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        if request.method == 'POST' and request.FILES['myfile']:
            submit = UploadAssignment()
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            # filestore = request.POST.get("filename")
            submit.file= request.POST.get("myfile")
            submit.course = request.POST.get("course")
            submit.assignment = request.POST.get("assignment")
            submit.description = request.POST.get("description")
            submit.save()


            # submit = UploadAssignment( assignment='assignment',description='description', myfile ='myfile' )

            # print("HI")
            submit.save()
        else:
            noy = 'did subbmit'
            return render({'noy': noy})

def show_submit_assignment(request):
    allsubmissions = AssignmentUpload.objects.all()
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    announcements = Annoucement.objects.all()
    item = len(announcements)

    # for teacher in teachers:
        

    for student in students:
        student

        print(student) 
    context = {
        "allsubmissions": allsubmissions,
        "teachers": teachers,
        "students": students,
        'item': item,
    }
    # print(student)
    return render(request, "students/submission_list.html", context)