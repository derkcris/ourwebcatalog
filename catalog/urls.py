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
    url(r'^category/$', views.category_index, name='category_index'),
    url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
    url(r'^category/add', views.category_add, name='category_add'),
    url(r'^category/(?P<category_id>\d+)/edit', views.category_edit, name='category_edit'),
    url(r'^category/(?P<category_id>\d+)/save', views.category_save, name='category_save'),
    url(r'^category/(?P<category_id>\d+)/remove', views.category_remove, name='category_remove'),
    url(r'^item/(?P<item_id>\d+)', views.item, name='item'),
)
