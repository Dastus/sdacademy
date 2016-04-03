from feedbacks.models import Feedback
from django.forms import ModelForm

class FeedbackModelForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'subject', 'message', 'from_email']