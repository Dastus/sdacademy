from django.contrib import admin
from .models import Student
from .forms import StudentModelForm
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display= ['full_name', 'email', 'skype']
    list_filter = ['courses']
    fieldsets = [('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
                 ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
                 (None, {'fields':['courses']})]
    filter_horizontal = ('courses',)
    search_fields = ['surname', 'email']
admin.site.register(Student, StudentAdmin)
