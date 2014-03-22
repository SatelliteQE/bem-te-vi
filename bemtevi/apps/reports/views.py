import json

from django.http import HttpResponse, Http404
from django.views.generic import View
from bemtevi.apps.reports.models import TestimonyEntry


class TestimonyEntryView(View):
    def get(self, request, *args, **kwargs):
        raise Http404()

    def post(self, request, *args, **kwargs):
        data = request.POST.get('testimony_data', None)
        if not data is None:
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
