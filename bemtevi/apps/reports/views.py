import json

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, Http404
from django.views.generic import View, RedirectView, TemplateView

from bemtevi.apps.reports.models import TestimonyEntry


class IndexView(RedirectView):
    url = reverse_lazy('testimony_report')


class MilestoneReportView(TemplateView):
    template_name = 'reports/milestone.html'


class TestimonyReportView(TemplateView):
    template_name = 'reports/testimony.html'

    def get(self, request, *args, **kwargs):
        self.entries = int(request.GET.get('entries', '7'))
        return super(
            TestimonyReportView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TestimonyReportView, self).get_context_data(**kwargs)
        context['api'] = TestimonyEntry.objects.filter(
            path__endswith='api')[:self.entries:-1]
        context['cli'] = TestimonyEntry.objects.filter(
            path__endswith='cli')[:self.entries:-1]
        context['ui'] = TestimonyEntry.objects.filter(
            path__endswith='ui')[:self.entries:-1]
        return context
