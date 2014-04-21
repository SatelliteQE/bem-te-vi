from django.conf.urls import patterns, url
from bemtevi.apps.reports.views import MilestoneReportView, TestimonyReportView

urlpatterns = patterns('',
    url(r'^milestone/$', MilestoneReportView.as_view(),
        name='milestone_report'),
    url(r'^testimony/$', TestimonyReportView.as_view(),
        name='testimony_report'),
)
