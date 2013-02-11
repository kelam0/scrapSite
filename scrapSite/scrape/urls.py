from django.conf.urls import patterns, include, url

urlpatterns = patterns('scrape.views',
    url(r'^$', 'index'),
    url(r'^(?P<spot_date,hour>\d+)/$', 'detail'),
)