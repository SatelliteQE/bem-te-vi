import datetime

from django.db import models


class TestimonyEntry(models.Model):
    date = models.DateField(default=datetime.date.today)
    path = models.CharField(max_length=100)
    testcases = models.PositiveIntegerField()
    manual_testcases = models.PositiveIntegerField()
    automated_testcases = models.PositiveIntegerField()
    no_docstring_testcases = models.PositiveIntegerField()

    class Meta:
        ordering = ['date']
