from rest_framework import serializers

from bemtevi.apps.reports.models import TestimonyEntry


class TestimonyEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestimonyEntry
        fields = ('date', 'path', 'testcases', 'manual_testcases',
                  'automated_testcases', 'no_docstring_testcases')
