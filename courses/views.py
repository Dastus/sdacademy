from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course
from .models import Lesson
from coaches.views import Coach
from .forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy

# Create your views here.
class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        pk = self.get_object().pk
        courses = Course.objects.filter(pk=pk)
        lessons_all = Lesson.objects.filter(course=courses)
        context['lessons_all'] = lessons_all
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = "courses/add.html"
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        title = "Course creation"
        context['title'] = title
        return context

    def form_valid(self, form):
        course = form.save()
        message = ("Course %s has been successfully added." % course.name)
        messages.success(self.request, message)
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        title = "Course update"
        context['title'] = title
        return context

    def form_valid(self, form):
        message = "The changes have been saved."
        messages.success(self.request, message)
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    context_object_name = "course"
    template_name= 'courses/remove.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        title = "Course deletion"
        context['title'] = title
        return context

    def get_success_url(self):
        course = super(CourseDeleteView, self).get_object()
        message = ('Course %s has been deleted.' % (course.name))
        messages.success(self.request, message)
        return reverse('index')


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
