from django.conf.urls import patterns, url
from loans import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<article_id>\d+)', views.article, name='article'),
    url(r'^item/(?P<item_id>\d+)', views.item, name='item')
)
