from django.conf.urls import patterns, include, url
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^post/(?P<pk>[0-9]+)/editcomment$', views.comment_remove, name='comment_edit'),
    url(r'^post/(?P<pk>[0-9]+)/addcomment$', views.comment_add, name='comment_add'),
    url(r'^search/$', views.search, name='search'),
   

)