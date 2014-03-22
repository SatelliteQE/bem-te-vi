from django.conf.urls import patterns, url
from bemtevi.apps.reports.views import TestimonyEntryView

urlpatterns = patterns('',
    url(r'^testimony/entry/$', TestimonyEntryView.as_view(),
        name='testimony_entry'),
)
