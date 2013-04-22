from django.conf.urls import patterns, url
from loans import views

urlpatterns = patterns(
    '',
    url(r'^$', views.dependency_index, name='dependency_index'),
    url(r'^dependency/$', views.dependency_index, name='dependency_index'),
    url(r'^dependency/(?P<dependency_id>\d+)/$', views.dependency, name='dependency'),
    url(r'^dependency/add', views.dependency_add, name='dependency_add'),
    url(r'^dependency/(?P<dependency_id>\d+)/edit', views.dependency_edit, name='dependency_edit'),
    url(r'^dependency/(?P<dependency_id>\d+)/save', views.dependency_save, name='dependency_save'),
    url(r'^dependency/(?P<dependency_id>\d+)/remove', views.dependency_remove, name='dependency_remove'),
    url(r'^dependency/(?P<dependency_id>\d+)/people/add', views.dependency_people_add, name='dependency_people_add'),
)
