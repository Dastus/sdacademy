from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentModelForm
from django import forms
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy

# Create your views here.
class StudentDetailView(DetailView):
    model = Student
    context_object_name = "student"
    template_name = "students/detail.html"


class StudentListView(ListView):
    model = Student
    template_name = "students/list.html"
    context_object_name = "students"

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses__id=course_id)
        else:
            students = Student.objects.all()
        return students


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
        student = super(StudentDeleteView, self).get_object()
        message = ('Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        messages.success(self.request, message)
        return context
