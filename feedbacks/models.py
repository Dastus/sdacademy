from django.db import models
from django.forms import ModelForm

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateTimeField(auto_now= True)
    def __unicode__(self):
        return self.name
