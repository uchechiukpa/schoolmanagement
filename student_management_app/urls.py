from django.urls import path, include
from . import views, HodViews, TeacherViews, StudentViews
from cmd_project import settings

urlpatterns = [
    path('doLogin/',views.doLogin, name='do_login'),
    path('', views.logout_user, name='do_logout'),
    path('showLogin', views.ShowLoginPage, name='show_login'),
    path('admin_home',HodViews.admin_home, name='admin_home'),
    
    
    path('get_user_details', views.GetUserDetails),
    path('user_details', views.UserDetails, name='user_detail'),
    path('add_teacher',HodViews.add_teacher,name="add_teacher"),
    # path('studentList',HodViews.studentList,name="studentList"),
    path('add_teacher_save',HodViews.add_teacher_save,name="add_teacher_save"),
    path('add_student', HodViews.add_student,name="add_student"),
    path('add_student_save', HodViews.add_student_save,name="add_student_save"),
    path('student_all', HodViews.student_list, name="student_list"),
    path('announcements', HodViews.show_annocements, name="show_annocements"),


    # studentView
    path('home', StudentViews.student_dashboard, name="student_dashboard"),
    path('student_home', StudentViews.student_home, name="student_home"),
    path('profile', StudentViews.student_profile, name="student_profile"),
    path('upload/<slug>/', StudentViews.upload_assignment, name="upload"),
    path('studentsgradelist', StudentViews.studentsgradeList, name="studentsgradelist"),
    path('student_home',StudentViews.student_home, name='student_home'),
    path('assignment/<slug>/', StudentViews.show_assignments, name='show_assignments'),
    path('submission/<slug>/', StudentViews.show_submissions, name='show_submissions'),
    # path('assignment', StudentViews.show_assignments, name='show_assignments'),
    # TeacherViews
    path('teacher_home', TeacherViews.teacher_home, name="teacher_home"),
    path('add_student_grade/',TeacherViews.GradeStudentView, name="grade_students" ),
    path('announcement',TeacherViews.annoucements_list, name="teacher_announcement" ),
    path('gradelist', TeacherViews.studentgradeList, name="gradelist"),
    
    
    path('all_submissions', TeacherViews.show_submit_assignment, name="all_submissions"),
    # path('submit_assignment',StudentViews.submit_assignment, name='submit_assignment'),
    path('add_submit_assignment',TeacherViews.add_submit_assignment, name='add_submit_assignment'),
    # path('gradestudents', TeacherViews.grade_students, name="grade_students"),
    
    
    ]