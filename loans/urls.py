from django.conf.urls import patterns, url
from loans import views

urlpatterns = patterns(
    '',
    url(r'^$', views.item_availables, name='loan_index'),
    url(r'^(?P<loan_id>\d+)/$', views.loan, name='loan'),
    url(r'^items/availables/$', views.item_availables, name='item_availables'),
    url(r'^items/on_loan/$', views.item_on_loan, name='item_on_loan'),
    url(r'^items/returned/$', views.item_returned, name='item_returned'),
    url(r'^items/add/(?P<item_id>\d+)/$', views.loan_add, name='loan_add'),
    url(r'^items/save/(?P<item_id>\d+)/$', views.loan_save, name='loan_save'),
    url(r'^items/return/(?P<loan_id>\d+)/$', views.loan_return, name='loan_return'),
    url(r'^items/return/(?P<loan_id>\d+)/save/$', views.loan_return_save, name='loan_return_save'),
    url(r'^dependency/$', views.dependency_index, name='dependency_index'),
    url(r'^dependency/(?P<dependency_id>\d+)/$', views.dependency, name='dependency'),
    url(r'^dependency/add', views.dependency_add, name='dependency_add'),
    url(r'^dependency/(?P<dependency_id>\d+)/edit', views.dependency_edit, name='dependency_edit'),
    url(r'^dependency/(?P<dependency_id>\d+)/save', views.dependency_save, name='dependency_save'),
    url(r'^dependency/(?P<dependency_id>\d+)/remove', views.dependency_remove, name='dependency_remove'),
    url(r'^dependency/(?P<dependency_id>\d+)/people/add', views.dependency_people_add, name='dependency_people_add'),
    url(r'^people/$', views.people_index, name='people_index'),
    url(r'^people/(?P<people_id>\d+)/$', views.people, name='people'),
    url(r'^people/(?P<people_id>\d+)/returned/$', views.people_returned, name='people_returned'),
    url(r'^people/add', views.people_add, name='people_add'),
    url(r'^people/(?P<people_id>\d+)/edit', views.people_edit, name='people_edit'),
    url(r'^people/(?P<people_id>\d+)/save', views.people_save, name='people_save'),
    url(r'^people/(?P<people_id>\d+)/remove', views.people_remove, name='people_remove'),
)
