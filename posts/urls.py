from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from posts.views import register, register_success, logout_page, home, create, create_success, show, project, message, message_send, inbox, answer, backed, donated, payment, search

urlpatterns = [
    url(r'^logout/$', logout_page, name='logout_page'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^register/success/$', register_success, name='register_success'),
    url(r'^home/$', home, name='home'),
    url(r'^create/$', create, name='create'),
    url(r'^create/success/$', create_success, name='create_success'),
    url(r'^show/$', show, name='show'),
    url(r'^project/(?P<project_id>\d+)/$',project, name='project'),
    url(r'^message/(?P<project_id>\d+)/$',message, name='message'),
    url(r'^answer/(?P<message_id>\d+)/$',answer, name='answer'),
    url(r'^message/success/$',message_send,name='message_send'),
    url(r'^inbox/$',inbox,name='inbox'),
    url(r'^backed/$',backed,name='backed'),
    url(r'^donated/$', donated,name='donated'),
    url(r'^payment/(?P<project_id>\d+)/(?P<ammountproxy>\d+)/$', payment,name='payment'),
    url(r'^search/$', search,name='search')
]
