from django.core.urlresolvers import reverse
from django.test import TestCase


class MilestoneReportTestCase(TestCase):
    def test_have_route(self):
        response = self.client.get(reverse('milestone_report'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('reports/milestone.html')


class TestimonyReportTestCase(TestCase):
    def test_report_data(self):
        response = self.client.get(reverse('testimony_report'))
        self.assertEqual(response.status_code, 200)

        self.assertIn('api', response.context)
        self.assertIn('cli', response.context)
        self.assertIn('ui', response.context)
