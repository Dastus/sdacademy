from django.db import models
from students.models import Student
from courses.models import Course
from django.forms import ModelForm

class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'address', 'skype', 'courses']
        #fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'address', 'skype']
        #help_texts={'courses':"Hold down \"Control\", or \"Command\" on a Mac, to select more than one1."}
