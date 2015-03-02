from django.conf.urls import patterns, include, url
from users.views import create
from users.views import activate


urlpatterns = patterns('',
    url(r'^new/', create, name="new"),
    url(r'^activate/(\w{50})$', activate, name='activate'),
)