from django.shortcuts import render
from django.contrib.auth.models import User
from courses.models import Course
from .models import Coach
# Create your views here.
def detail(request, coach_id):
    coach = Coach.objects.filter(id=coach_id)
    fullname = Coach.objects.get(id=coach_id).user.get_full_name()
    email = Coach.objects.get(id=coach_id).user.email
    course_coach = Course.objects.filter(coach=coach_id)
    course_assistant = Course.objects.filter(assistant=coach_id)
    return render(request, 'coaches/detail.html', {'coach': coach,
                                                   'fullname': fullname,
                                                   'email': email,
                                                   'course_coach': course_coach,
                                                   'course_assistant': course_assistant})