from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',
    # ex: /quadratic/results/?a=5&b=6&c=2
    url(r'^results/$', views.quadratic_results, name='results'),
)