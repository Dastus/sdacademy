from courses.models import Course
from courses.models import Lesson
from django.forms import ModelForm

class CourseModelForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'short_description', 'description', 'coach', 'assistant']


class LessonModelForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ['subject', 'description', 'course', 'order']