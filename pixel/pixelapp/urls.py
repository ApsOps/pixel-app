from django.conf.urls import patterns, url
from pixelapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)