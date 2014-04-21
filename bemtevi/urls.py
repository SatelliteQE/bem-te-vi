from django.conf.urls import patterns, include, url

from bemtevi.apps.reports.views import IndexView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('bemtevi.apps.reports.api.urls')),
    url(r'^reports/', include('bemtevi.apps.reports.urls')),
)
