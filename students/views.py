from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentModelForm
from django import forms
from django.contrib import messages
#from courses.models import Course
#from courses.models import Lesson
# Create your views here.

def list_view(request):
    course_id = request.GET.get('course_id','err')
    students_all = Student.objects.all()
    if course_id == 'err':
        return render(request, 'students/list.html', {'students_all': students_all})
    else:
        students_all = Student.objects.filter(courses=course_id)
        return render(request, 'students/list.html', {'students_all': students_all})
    '''
    try:
        cid = int(request.GET.get('course_id', '')[0])
        students = Student.objects.filter(courses=cid)
        return render(request, 'students/list.html', {'students': students})
    except IndexError:
        students = Student.objects.all()
        return render(request, 'students/list.html', {'students': students}
    '''
def detail(request, student_id):
        student = Student.objects.filter(id=student_id)
        return render(request, 'students/detail.html', {'student': student})

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, ('Student %s %s has been successfully added.' % (student.name, student.surname)))
            return redirect('/students')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            app = form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
    student = Student.objects.get(pk=student_id)
    credentials = "%s %s" % (student.name, student.surname)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Info on %s  has been sucessfully deleted.' % credentials)
        return redirect('/students')
    return render(request, 'students/remove.html', {'credentials': credentials})