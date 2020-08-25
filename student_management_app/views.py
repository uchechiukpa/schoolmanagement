from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse 
from django.contrib import messages

from student_management_app.models import Student 
from student_management_app.EmailBackEnd import EmailBackEnd
# Create your views here.


def ShowLoginPage(request):
    return render(request, 'login_page.html')


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")

    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            print(user.user_type)
            if user.user_type=="1":
                print(user.user_type)
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("teacher_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request, "Invalid Login Details")
            # return HttpResponse("<h2>invalid login</h2>")
            return HttpResponseRedirect("/")




def GetUserDetails(request):
    
    if request.user!=None:
        # return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type) + request.user.username + request.user.first_name + request.user.student.student_id)
        context = {
            'request.user.email': request.user.email,
            'request.user.username': request.user.username,
            'request.user.first_name ':  request.user.first_name,
            'request.user.student.student_id': request.user.student.student_id,
            'request.user.last_name': request.user.last_name
        }
        return render(request, 'student_layout.html', context)
    else:
        return HttpResponse("Please Login First")

def UserDetails(request):
     if request.user!=None:
        users = request.user
        students = Student.objects.get(pk = 1)
        print(students.student_id)
        context = {
            'students':students,
            'users': users
            
        }
        return render(request, 'students/student_detail.html', {'context': context})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
