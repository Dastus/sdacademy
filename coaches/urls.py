from django.conf.urls import url
from coaches import views

app_name = 'coaches'
urlpatterns = [
    #url((r'^$'), views.detail, name='detail'),
    url((r'^(?P<coach_id>[1-9]+)/$'), views.detail, name='detail'),
]