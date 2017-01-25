from django.conf.urls import url
from loginsys.views import *

urlpatterns = [
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', register),
    url(r'^register/(?P<secret_key>\w+)/$', confirm_registration),
]