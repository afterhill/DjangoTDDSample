
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'lists.views.home_page', name='home'),
                       url(r'^accounts/', include('accounts.urls')),
                       url(r'^lists/', include('lists.urls')),

                       )
