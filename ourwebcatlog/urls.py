from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalog import views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ourwebcatlog.views.home', name='home'),
    # url(r'^ourwebcatlog/', include('ourwebcatlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^loans/', include('loans.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
