from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'landing.views.home', name='home'),
    url(r'^ponentes/$', 'landing.views.speakers', name='speakers'),
    url(r'^el-evento/$', 'landing.views.event', name='event'),
    url(r'^talleres/$', 'landing.views.workshops', name='workshops'),
    url(r'^programa/$', 'landing.views.agenda', name='agenda'),
    url(r'^patrocinar/$', 'landing.views.sponsor_form', name='sponsor_form'),
    url(r'^voluntario/$', 'landing.views.sponsor_form', {'register_type': 'volunteer'},name='volunteer'),
    url(r'^blog/$', 'landing.views.post', name='blog'),
    url(r'^blog/(?P<post_slug>.+)/$', 'landing.views.post', name='post'),
    url(r'^frontend/', include('frontend.urls', namespace='front')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
)

urlpatterns += (
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)