from django.conf.urls import patterns, url
from bemtevi.apps.reports.views import TestimonyReportView, TestimonyEntryView

urlpatterns = patterns('',
    url(r'^testimony/$', TestimonyReportView.as_view(),
        name='testimony_report'),
    url(r'^testimony/entry/$', TestimonyEntryView.as_view(),
        name='testimony_entry'),
)
