from django.contrib import admin
from bemtevi.apps.reports.models import TestimonyEntry


class TestimonyEntryModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('path', 'testcases', 'automated_testcases',
                    'manual_testcases', 'no_docstring_testcases', 'date')
    list_filter = ('date', 'path')

admin.site.register(TestimonyEntry, TestimonyEntryModelAdmin)
