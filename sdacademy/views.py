from django.http import HttpResponse
from django.shortcuts import render

def contact(request):
    return HttpResponse("It's contact page")

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def student_detail(request):
    return render(request, 'student_detail.html')

def student_list(request):
    return render(request, 'student_list.html')
