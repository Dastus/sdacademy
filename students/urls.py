from django.conf.urls import url
from students import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    #url((r'^(?P<student_id>[1-9]+)/$'), views.list_view, name='list_view'),
    url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),
]