from website.views import  HomePageTemplateView, MovieDetailView, GenderListView, StarDetailView

__author__ = 'Nataliel Vasconcelos'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', HomePageTemplateView.as_view(), name='home'),
    url(r'^ator/(?P<slug>[\w_-]+)$', StarDetailView.as_view(), name='star_detail'),
    url(r'^(?P<gender>[\w_-]+)/$', GenderListView.as_view(), name='gender_list'),
    url(r'^(?P<gender>[\w_-]+)/(?P<slug>[\w_-]+)$', MovieDetailView.as_view(), name='movie_detail'),

)
