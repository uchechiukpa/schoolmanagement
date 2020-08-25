from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('announcement/', include('announcements.urls')),
    # path('department/', include('departments.urls')),
    # path('course/', include('courses.urls')),
    # path('assigment/', include('assignments.urls')),
    # path('class/', include('classes.urls')),
    # path('lecture/', include('lectures.urls')),
    # path('report/', include('reports.urls')),
    # path('submission/', include('submissions.urls')),
    # path('teacher/', include('teachers.urls')),
    # path('student/', include('students.urls')),
    path('', include('student_management_app.urls')),

]


# urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)