from django.shortcuts import render
from .forms import TeacherForm, StudentForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def update_profile(request):
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
        student_form = StudentForm(request.POST)
        if teacher_form.is_valid() and student_form.is_valid():
            teacher_form.save()
            student_form.save()
            messages.success(request, _('your profile was successfully updated '))
            return redirect ('settings: profile')
        else:
            messages.error(request, _('please correct the error below'))
    else:
        teacher_form = TeacherForm()
        student_form = StudentForm()
    return render(request, 'accounts/account.html', {
        'teacher_form': teacher_form,
        'student_form': student_form

    })