from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from bemtevi.apps.reports.api.views import TestimonyEntryCreateAPIView


urlpatterns = patterns('',
    url(r'^reports/testimony-entry$', TestimonyEntryCreateAPIView.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
