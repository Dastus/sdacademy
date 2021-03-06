from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from feedbacks import views as feedback

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^student_list/', views.student_list, name='student_list'),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^student_detail/', views.student_detail, name='student_detail'),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    #url(r'^feedback/$', include('feedbacks.urls')),
    url(r'^feedback/$', feedback.FeedbackView.as_view()),
) 
