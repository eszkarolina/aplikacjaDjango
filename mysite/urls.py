from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('mojblog.urls')),
    url(r'^users/', include('users.urls', namespace="users")),

    
)
