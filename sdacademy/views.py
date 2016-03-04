from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Course

def contact(request):
    return HttpResponse("It's contact page")

def index(request):
    courses_all = Course.objects.all()
    return render(request, 'index.html', {"courses_all":courses_all})

def contact(request):
    return render(request, 'contact.html')

def student_detail(request):
    return render(request, 'student_detail.html')

def student_list(request):
    return render(request, 'student_list.html')
