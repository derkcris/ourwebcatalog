from django.conf.urls import patterns, url
from catalog import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<article_id>\d+)/$', views.article, name='article'),
    url(r'^article/add', views.article_add, name='article_add'),
    url(r'^article/(?P<article_id>\d+)/edit', views.article_edit, name='article_edit'),
    url(r'^article/(?P<article_id>\d+)/save', views.article_save, name='article_save'),
    url(r'^article/(?P<article_id>\d+)/remove', views.article_remove, name='article_remove'),
    url(r'^article/(?P<article_id>\d+)/item/add', views.item_add, name='item_add'),
    url(r'^item/(?P<item_id>\d+)', views.item, name='item'),
)
