from django.conf.urls import url
from articles.views import *

urlpatterns = [
    url(r'^articles/all/', articles),
    url(r'^articles/(?P<article_id>\d+)/', article),
    url(r'^articles/addcomment/(?P<article_id>\d+)/', addcomment),
    url(r'^articles/page/(\d+)/$', articles),


]