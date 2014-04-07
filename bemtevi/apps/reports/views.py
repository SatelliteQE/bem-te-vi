import json

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, Http404
from django.views.generic import View, RedirectView, TemplateView

from bemtevi.apps.reports.models import TestimonyEntry


class IndexView(RedirectView):
    url = reverse_lazy('testimony_report')


class TestimonyReportView(TemplateView):
    template_name = 'reports/testimony.html'

    def get_context_data(self, **kwargs):
        context = super(TestimonyReportView, self).get_context_data(**kwargs)
        context['api'] = TestimonyEntry.objects.filter(
            path__endswith='api')[:7]
        context['cli'] = TestimonyEntry.objects.filter(
            path__endswith='cli')[:7]
        context['ui'] = TestimonyEntry.objects.filter(
            path__endswith='ui')[:7]
        return context


class TestimonyEntryView(View):
    def get(self, request, *args, **kwargs):
        raise Http404()

    def post(self, request, *args, **kwargs):
        data = request.POST.get('testimony_data', None)
        if data is not None:
            data = json.loads(data)
            for summary in data:
                entry = TestimonyEntry()
                entry.testcases = summary['tc_count']
                entry.automated_testcases = summary['auto_count']
                entry.manual_testcases = summary['manual_count']
                entry.no_docstring_testcases = summary['no_docstring']
                entry.path = summary['path']
                entry.save()
            return HttpResponse('ok')
        else:
            return HttpResponse('error')
