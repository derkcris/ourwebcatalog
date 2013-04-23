from django.conf.urls import patterns, url
from loans import views

urlpatterns = patterns(
    '',
    url(r'^$', views.loan_availables, name='loan_index'),
    url(r'^availables/$', views.loan_availables, name='loan_availables'),
    url(r'^add/(?P<item_id>\d+)/$', views.loan_add, name='loan_add'),
    url(r'^save/(?P<item_id>\d+)/$', views.loan_save, name='loan_save'),
    url(r'^dependency/$', views.dependency_index, name='dependency_index'),
    url(r'^dependency/(?P<dependency_id>\d+)/$', views.dependency, name='dependency'),
    url(r'^dependency/add', views.dependency_add, name='dependency_add'),
    url(r'^dependency/(?P<dependency_id>\d+)/edit', views.dependency_edit, name='dependency_edit'),
    url(r'^dependency/(?P<dependency_id>\d+)/save', views.dependency_save, name='dependency_save'),
    url(r'^dependency/(?P<dependency_id>\d+)/remove', views.dependency_remove, name='dependency_remove'),
    url(r'^dependency/(?P<dependency_id>\d+)/people/add', views.dependency_people_add, name='dependency_people_add'),
    url(r'^people/$', views.people_index, name='people_index'),
    url(r'^people/(?P<people_id>\d+)/$', views.people, name='people'),
    url(r'^people/add', views.people_add, name='people_add'),
    url(r'^people/(?P<people_id>\d+)/edit', views.people_edit, name='people_edit'),
    url(r'^people/(?P<people_id>\d+)/save', views.people_save, name='people_save'),
    url(r'^people/(?P<people_id>\d+)/remove', views.people_remove, name='people_remove'),
)
