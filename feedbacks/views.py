from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback
from .forms import FeedbackModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.mail import mail_admins

# Create your views here.
class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    #feedbacks/feedback_form.html
    success_url = '/feedback'


    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        title = "Create feedback"
        context['title'] = title
        return context

    def form_valid(self, form):
        feedback = form.save()
        mail_admins(feedback.subject, feedback.message)
        message = ("Thank you for your feedback! We will keep in touch with you very soon!")
        messages.success(self.request, message)
        return super(FeedbackView, self).form_valid(form)

