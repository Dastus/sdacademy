from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import Coach

class CoachAdmin(admin.ModelAdmin):
    list_display = ['get_first_name', 'get_last_name', 'gender', 'skype', 'description']
    list_filter = ('user__is_staff',)

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_is_staff(self, obj):
        return obj.user.is_staff

admin.site.register(Coach, CoachAdmin)
'''
class LessonInline(admin.TabularInline):
    model = Lesson
    #fieldsets = [(None,{'fields': ['subject', 'description']}), ('Extended info', {'fields': ['order']})]

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']
    inlines = [LessonInline]
    search_fields = ['name']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
'''