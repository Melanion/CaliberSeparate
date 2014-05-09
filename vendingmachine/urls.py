from django.conf.urls import patterns, url

from vendingmachine import views

urlpatterns = patterns('',
    url(r'^$', 'vendingmachine.views.start', name='start'),
    url(r'^license/$', 'vendingmachine.views.license', name='license'),
)