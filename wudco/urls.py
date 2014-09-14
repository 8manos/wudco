from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'landing.views.home', name='home'),
    url(r'^ponentes/$', 'landing.views.speakers', name='speakers'),
    url(r'^talleres/$', 'landing.views.workshops', name='workshops'),
    url(r'^frontend/', include('frontend.urls', namespace='front')),
    url(r'^admin/', include(admin.site.urls)),
)
