from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'imnet.views.index', name='home'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'imnet/login.html'}),
    (r'^accounts/', include('registration.urls')),
    url(r'^artists/$', 'imnet.views.artists'),
    url(r'^artists/(?P<artist_id>\d+)/$', 'imnet.views.artist'),
    # url(r'^IMNet/', include('IMNet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^messages/', include('messages.urls')),
    url(r'^lookup/user/(?P<username>\w+)/$', 'imnet.views.user_lookup'),

)

urlpatterns += staticfiles_urlpatterns()
