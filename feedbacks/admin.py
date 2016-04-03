from django.contrib import admin
from .models import Feedback
from .forms import FeedbackModelForm
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display= ['from_email', 'create_date']
    '''
    list_filter = ['courses']
    fieldsets = [('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
                 ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
                 (None, {'fields':['courses']})]
    filter_horizontal = ('courses',)
    search_fields = ['surname', 'email']
    '''
admin.site.register(Feedback, FeedbackAdmin)