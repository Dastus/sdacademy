from django.conf.urls import url
from courses import views

app_name = 'courses'
urlpatterns = [
    url((r'^$'), views.detail, name='detail'),
    url((r'^(?P<course_id>[1-9]+)/$'), views.detail, name='detail'),
]
