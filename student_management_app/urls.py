from django.urls import path, include
from . import views, HodViews, TeacherViews, StudentViews
from cmd_project import settings

urlpatterns = [
    path('doLogin/',views.doLogin, name='do_login'),
    path('showLogin', views.ShowLoginPage, name='show_login'),
    path('admin_home',HodViews.admin_home, name='admin_home'),
    path('get_user_details', views.GetUserDetails),
    path('add_teacher',HodViews.add_teacher,name="add_teacher"),
    path('add_teacher_save',HodViews.add_teacher_save,name="add_teacher_save"),
    path('add_student', HodViews.add_student,name="add_student"),
    path('add_student_save', HodViews.add_student_save,name="add_student_save"),
    path('add_subject', HodViews.add_subject,name="add_subject"),
    path('add_subject_save', HodViews.add_subject_save,name="add_subject_save"),
    path('teacher_home', TeacherViews.teacher_home, name="teacher_home"),
    path('student_home', StudentViews.student_home, name="student_home"),
]