from django.shortcuts import render
from django.contrib import messages 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  UploadAssignmentForm, AssignmentForm
from student_management_app.models import CustomUser, Teacher, Student
from announcements.models import Annoucement
from assignments.models import Assignment 
from courses.models import Course
from django.db.models  import Count
from submissions.models import Submission, UploadAssignment, StudentGrade
from django.conf import settings
# from assignments.models import Assignment 
from django.core.files.storage import FileSystemStorage
from upload.models import AssignmentUpload
from courses.models import Course



def student_home(request):
    courses =  Course.objects.all()
    submissions = Submission.objects.all()
    class_id = request.user.student.student_id
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

    course_list = []
    for assignment in assignments:

        course_list.append(assignment.course_id.course_name)
        assignment = assignment.course_id.course_class

    sortedassignments = list(dict.fromkeys(course_list))

    # print(assignment)

    context = {
        'courses': courses, 
        'submissions': submissions,
        'assignments': assignments,
        'announcements': announcements,
        'item': item,
        'class_name': class_name,
        'sortedassignments': sortedassignments,
        'assignment': assignment
    }

    # print(sortedassignments)

   

    

    return render(request, 'students/students_home.html', context)


def student_profile(request):
    announcements = Annoucement.objects.all()
   
    item = len(announcements)
    return render(request, "professor_profile.html", {"announcements":announcements, "item": item})

def student_dashboard(request):
    return render(request, "students/student_dashboard.html")

def studentsgradeList(request):
    students= Student.objects.all()
    studentgrades = StudentGrade.objects.all()
    announcements = Annoucement.objects.all()
    assignments = Assignment.objects.all()
    courses =  Course.objects.all()
    submissions = Submission.objects.all()
    
   
    item = len(announcements)
    gradedstudents=[]
    for studentgrade in studentgrades:
        for student in students:

            if studentgrade.student_name == student.admin.first_name + " " + student.admin.last_name:
                gradedstudents.append(studentgrade)

    users = studentgrade.student_name.split()

    
    usercourses=[]
    usercourses.append(request.user.first_name)
    usercourses.append(request.user.last_name)
    s = " "
    user= s.join(usercourses)
    
    context = {
        'assignments': assignments,
        'courses':courses,
        'submissions': submissions,
        # 'coursedetails': coursedetails,
        'announcements': announcements,
        "gradedstudents": gradedstudents,
        "user": user,
        "item": item
    }
    return render(request, "students/gradelist.html", context)


def show_assignments(request,slug):
    assignments = Assignment.objects.all()
    courses =  Course.objects.all()
    submissions = Submission.objects.all()
    coursedetails = Course.objects.filter(course_name=slug)
    slug = slug 
    announcements = Annoucement.objects.all()
   
    item = len(announcements)
    # print(assignments)
    
        # print(assignment.upload_question)
    # print(assignments)
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


    context = {
        'assignments': assignments,
        'courses':courses,
        'announcements': announcements,
        'submissions': submissions,
        'coursedetails': coursedetails,
        'slug': slug,
        'class_name': class_name,
        'item': item,
        
    }

   

    # print(request.user.student.student_id)
    return render(request, 'students/assignments_list.html', context)


def show_submissions(request, slug):
    announcements = Annoucement.objects.all()
    item = len(announcements)
    students = Student.objects.all()
    assignments = Assignment.objects.all()
    courses =  Course.objects.all()
    submissions = Submission.objects.all()
    coursedetails = Course.objects.filter(course_name=slug)

    course_list = []
    for assignment in assignments:

        course_list.append(assignment.course_id.course_name)
        assignment = assignment.course_id.course_class

    sortedassignments = list(dict.fromkeys(course_list))

    for student in students:
        student.admin.first_name

        for submission in submissions:

            context = {
                'assignments': assignments,
                "courses": courses,
                'submissions': submissions,
                'coursedetails': coursedetails,
                "students": students,
                'sortedassignments': sortedassignments,
                'assignment': assignment,
                'item': item,
                # 'submissionlists': submissionlists
                'submission':submission 
                
            }


    return render(request, 'students/submissions_list.html', context)

def upload_assignment(request, slug):
    assignments = Assignment.objects.all()
    courses =  Course.objects.all()
    submissions = Submission.objects.all()
    # coursedetails = Course.objects.filter(course_name=slug)
    slug = slug 
    announcements = Annoucement.objects.all()
    item = len(announcements)

    if request.method == "POST":
        slug = slug
        form = AssignmentForm(request.POST, request.FILES)

        if form.is_valid():
            assignment = AssignmentUpload()
            assignment.student_name = form.cleaned_data["student_name"]
            assignment.submitted_assignment = form.cleaned_data["submitted_assignment"]
            assignment.save()
            saved = True   

            messages.success(request,"Assignment submitted")
            # return HttpResponseRedirect(reverse("submit_assignment"))
            return render(request, "students/upload_assignments.html",{"form":form, "slug": slug})
            # return redirect('students/upload_assignments.html')
    else: 

        form = AssignmentForm()

        context = {
            "form":form, 
            "slug": slug,
            'assignments': assignments,
            'courses':courses,
            'announcements': announcements,
            'submissions': submissions,
            'item': item,
           
        }
    return render(request, "students/upload_assignments.html", context)


