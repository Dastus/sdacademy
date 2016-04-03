from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .models import Student
from courses.models import Course
from .forms import StudentModelForm
from django import forms
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class StudentDetailView(DetailView):
    model = Student
    context_object_name = "student"
    template_name = "students/detail.html"
    paginate_by = 2


class StudentListView(ListView):
    model = Student
    template_name = "students/list.html"
    context_object_name = "students"
    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses__id=course_id)
        else:
            students = Student.objects.all()
        return students

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        course_id = self.request.GET.get('course_id', None)
        course_name = None
        if course_id:
            student_list = Student.objects.filter(courses__id=course_id)
            course = Course.objects.get(id=course_id)
            course_name = course.name
        else:
            student_list = Student.objects.all()
        paginator = Paginator(student_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            student_lists = paginator.page(page)
        except PageNotAnInteger:
            student_lists = paginator.page(1)
        except EmptyPage:
            student_lists = paginator.page(paginator.num_pages)
        context['student_lists'] = student_lists
        context['course_id'] = course_id
        context['course_name'] = course_name
        return context


class StudentCreateView(CreateView):
    model = Student
    #template_name = 'students/add.html'
    success_url = '/students'

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        title = "Student registration"
        context['title'] = title
        return context

    def form_valid(self, form):
        student = form.save()
        message = ("Student %s %s has been successfully added." % (student.name, student.surname))
        messages.success(self.request, message)
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    #template_name = 'students/edit.html'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        title = "Student info update"
        context['title'] = title
        return context

    def form_valid(self, form):
        message = "Info on the student has been sucessfully changed"
        messages.success(self.request, message)
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    #template_name= 'students/remove.html'
    success_url = '/students'

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        title = "Student info suppression"
        context['title'] = title
        return context

    def get_success_url(self):
        student = super(StudentDeleteView, self).get_object()
        message = ('Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        messages.success(self.request, message)
        return reverse('index')