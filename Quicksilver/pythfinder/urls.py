__author__ = 'adamthomson'

from django.conf.urls import patterns, url
from pythfinder import views

urlpatterns = patterns('',
    url(r'^$', views.index.index, name="index"),
    url(r'^character$', views.character.index, name="char_index"),
    url(r'^character/(?P<char_id>\d+)$', views.character.detail, name="char_detail"),
    url(r'^character/(?P<char_id>\d+)/level$', views.character.level_up, name="char_level"),
    url(r'^character/new$', views.character.char_new, name="char_new"),
)