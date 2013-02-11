from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'scrape.views.home'),
    url(r'^please_wait/$', 'scrape.views.please_wait'),
    url(r'^scraper/$', 'scrape.views.scraper'),                   
    url(r'^admin/', include(admin.site.urls)),
)
