from django.shortcuts import render, redirect
#from django.shortcuts import render_to_response
from django.contrib import messages
from .models import Course
from .models import Lesson
from coaches.views import Coach
from .forms import CourseModelForm, LessonModelForm

# Create your views here.
def detail(request, course_id):
    courses = Course.objects.filter(id=course_id)
    course = Course.objects.get(id=course_id)
    lessons_all = Lesson.objects.filter(course=courses)
    return render(request, 'courses/detail.html', {'courses': courses, 'lessons_all': lessons_all,
                                                      'particular_course':course.id, 'course':course,})
    '''
    coach_fullname = course.coach.user.get_full_name()
    assistant_fullname = course.assistant.user.get_full_name()
    return render(request, 'courses/detail.html', {'courses': courses, 'lessons_all': lessons_all,
                                                      'particular_course':course.id, 'course':course ,
                                                   'coach_fullname': coach_fullname,
                                                   'assistant_fullname':assistant_fullname })
                                                   '''


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, ('Course %s has been successfully added.' % course.name))
        return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})


def edit(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course %s has been deleted.' % course.name)
        return redirect('index')
    return render(request, 'courses/remove.html', {'name':course.name,})


def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Lesson %s has been successfully added." % form['subject'].value()))
            return redirect('/courses/%d' % int(course_id))
    else:
        form = LessonModelForm(initial={'course':course_id})
    return render(request, 'courses/add_lesson.html', {'form': form})
