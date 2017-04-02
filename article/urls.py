from django.conf.urls import url
from article.views import *

urlpatterns = [
    url(r'^$', require_login(show)),
    url(r'^(?P<id>\d+)/$', require_login(detail), name='detail'),
    url(r'^(?P<arch>\w+)/$', require_login(archives), name = 'archives'),
#    url(r'^tag(?P<tag>\w+)/$', search_tag, name = 'search_tag'),
]
