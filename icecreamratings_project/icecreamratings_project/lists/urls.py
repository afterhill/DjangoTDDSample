# from django.conf.urls import patterns, include, url
# from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#     url(r'^$', TemplateView.as_view(template_name='base.html')),

# Examples:
# url(r'^$', 'icecreamratings_project.views.home', name='home'),
# url(r'^icecreamratings_project/', include('icecreamratings_project.foo.urls')),

# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

# Uncomment the next line to enable the admin:
#     url(r'^admin/', include(admin.site.urls)),
# )

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^(.+)/$',
                           'lists.views.view_list', name='view_list'),
                       url(r'^(.+)/new_item$',
                           'lists.views.add_item', name='add_item'),
                       url(r'^new$',
                           'lists.views.new_list', name='new_list')
                       )
