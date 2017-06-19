from django.conf.urls import url
from articles.views import *

urlpatterns = [
    url(r'^all/', articles),
    url(r'^add/', newarticle),
    url(r'^(?P<article_id>\d+)/', article),
    url(r'^addcomment/(?P<article_id>\d+)/', addcomment),
    url(r'^page/(\d+)/$', articles),


]