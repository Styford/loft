from django.conf.urls import url
from sandbox.views import *

urlpatterns = [

    url(r'^(?P<id_prog>\d+)/$', open_extprog),
    url(r'^$', widget),
]