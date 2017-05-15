from django.conf.urls import url
from article.views import *

urlpatterns = [
    url(r'^$', require_login(show)),
    url(r'^(?P<id>\d+)/$', require_login(detail), name='detail'),
    url(r'^new/$',require_login(post_new), name = 'post_new'),
    url(r'^(?P<arch>\w+)/$', require_login(archives), name = 'archives'),
]
