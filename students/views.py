from django.shortcuts import render
from .models import Student
from courses.models import Course
from courses.models import Lesson
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
        #student = student.name
        return render(request, 'students/detail.html', {'student': student})



