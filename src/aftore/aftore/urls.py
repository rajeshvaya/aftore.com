from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('auth.urls')),
    
    url(r'^.*$', 'aftore.views.index', name='home'), # default page for 404 not found
)