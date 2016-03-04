from django.shortcuts import render
#from django.shortcuts import render_to_response
from .models import Course
from .models import Lesson

# Create your views here.
def detail(request, course_id):
    courses = Course.objects.filter(id=course_id)
    course = Course.objects.get(id=course_id)
    lessons_all = Lesson.objects.filter(course=courses)
    return render(request, 'courses/detail.html', {'courses': courses, 'lessons_all': lessons_all,
                                                      'particular_course':course.id, 'course':course})
