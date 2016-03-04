from django.contrib import admin

# Register your models here.
from .models import Course
from .models import Lesson


admin.site.register(Course)
admin.site.register(Lesson)
