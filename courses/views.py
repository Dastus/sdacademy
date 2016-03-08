from django.shortcuts import render
#from django.shortcuts import render_to_response
from .models import Course
from .models import Lesson
from coaches.views import Coach

# Create your views here.
def detail(request, course_id):
    courses = Course.objects.filter(id=course_id)
    course = Course.objects.get(id=course_id)
    lessons_all = Lesson.objects.filter(course=courses)
    coach_fullname = course.coach.user.get_full_name()
    assistant_fullname = course.assistant.user.get_full_name()
    return render(request, 'courses/detail.html', {'courses': courses, 'lessons_all': lessons_all,
                                                      'particular_course':course.id, 'course':course ,
                                                   'coach_fullname': coach_fullname,
                                                   'assistant_fullname':assistant_fullname })
