from django.contrib import admin

# Register your models here.
from .models import Course
from .models import Lesson

class LessonInline(admin.TabularInline):
    model = Lesson

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']
    inlines = [LessonInline]
    search_fields = ['name']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
