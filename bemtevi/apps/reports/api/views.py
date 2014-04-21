from rest_framework import generics

from bemtevi.apps.reports.api.serializers import TestimonyEntrySerializer
from bemtevi.apps.reports.models import TestimonyEntry


class TestimonyEntryCreateAPIView(generics.CreateAPIView):
    """
    API endpoint that allows adding testimony entries.
    """
    queryset = TestimonyEntry.objects.all()
    serializer_class = TestimonyEntrySerializer
