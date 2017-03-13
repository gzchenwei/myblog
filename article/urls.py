from django.conf.urls import url
from article.views import *

urlpatterns = [
    url(r'^$', showall),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^archives/$', archives, name = 'archives'),
    url(r'^tag(?P<tag>\w+)/$', search_tag, name = 'search_tag'),
]
