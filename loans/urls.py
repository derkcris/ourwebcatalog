from django.conf.urls import patterns, url
from loans import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^catalog/$', views.article_index, name='article_index'),
    url(r'^catalog/article/(?P<article_id>\d+)', views.article, name='article'),
    url(r'^catalog/article/add', views.article_add, name='article_add'),
    url(r'^catalog/article/(?P<article_id>\d+)/edit', views.article_edit, name='article_edit'),
    url(r'^catalog/article/save', views.article_save, name='article_save'),
    url(r'^catalog/article/(?P<article_id>\d+)/save', views.article_save, name='article_save'),
    url(r'^catalog/article/(?P<article_id>\d+)/remove', views.article_remove, name='article_remove'),
    url(r'^catalog/item/add', views.item_add, name='item_add'),
    url(r'^catalog/item/(?P<item_id>\d+)', views.item, name='item'),
)
