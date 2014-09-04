from django.conf.urls import patterns, url
from frontend import views

urlpatterns = patterns('',
  url(r'^(?P<page>.+)$', views.page)
)
