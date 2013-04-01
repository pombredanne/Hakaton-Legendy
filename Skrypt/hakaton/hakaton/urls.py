from django.conf.urls.defaults import *
from hakaton.views import SearchLegend

urlpatterns = patterns('',
    ('^SearchLegend/$', SearchLegend),
)