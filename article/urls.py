from django.conf.urls import url
from article.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', showall),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^(?P<arch>\w+)/$', archives, name = 'archives'),
#    url(r'^tag(?P<tag>\w+)/$', search_tag, name = 'search_tag'),
]
