import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase
from bemtevi.apps.reports.models import TestimonyEntry


class TestimonyReportTestCase(TestCase):
    def test_report_data(self):
        response = self.client.get(reverse('testimony_report'))
        self.assertEqual(response.status_code, 200)

        self.assertIn('api', response.context)
        self.assertIn('cli', response.context)
        self.assertIn('ui', response.context)


class TestimonyEntryTestCase(TestCase):
    def test_get_testimony_entry_404(self):
        """Returns 404 when GET on the testimony entry URL"""
        response = self.client.get(reverse('testimony_entry'))
        self.assertEqual(response.status_code, 404)

    def test_receive_testimony_entry(self):
        """Could receive a testimony entry"""
        json_string = (
            '[{"path":"api", "auto_count": 24, "manual_count": 67, '
            '"auto_percent": 26.373626373626372, "no_docstring": 0, '
            '"tc_count": 91, "manual_percent": 73.62637362637362}, '
            '{"path":"cli", "auto_count": 114, "manual_count": 258, '
            '"auto_percent": 30.64516129032258, "no_docstring": 0, '
            '"tc_count": 372, "manual_percent": 69.35483870967742}, '
            '{"path":"ui", "auto_count": 102, "manual_count": 278, '
            '"auto_percent": 26.842105263157894, "no_docstring": 0, '
            '"tc_count": 380, "manual_percent": 73.15789473684211}]')

        response = self.client.post(reverse('testimony_entry'),
                                    {'testimony_data': json_string})
        self.assertEqual(response.content, 'ok')

        entries = TestimonyEntry.objects.all()
        self.assertEqual(len(entries), 3)

        today = datetime.date.today()
        entries_data = (
            (today, 91, 24, 67, 0, 'api'),
            (today, 372, 114, 258, 0, 'cli'),
            (today, 380, 102, 278, 0, 'ui'),
        )

        for entry, data in zip(entries, entries_data):
            self.assertEqual(entry.date, data[0])
            self.assertEqual(entry.testcases, data[1])
            self.assertEqual(entry.automated_testcases, data[2])
            self.assertEqual(entry.manual_testcases, data[3])
            self.assertEqual(entry.no_docstring_testcases, data[4])
            self.assertEqual(entry.path, data[5])
