from django.conf.urls import url
from django.contrib import admin
from board.views import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^project/(?P<pk>[0-9]+)/$', ProjectView.as_view(), name='project_url'),
    url(r'^project/(?P<pk>[0-9]+)/create-story/$', StoryCreate.as_view(), name='create_story'),
    url(r'^project/(?P<pk>[0-9]+)/create-sprint/$', SprintCreate.as_view(), name='create_sprint'),
]
