__author__ = 'adamthomson'

from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Quicksilver import views

urlpatterns = patterns(
    url(r'^$',
            views.index.index, name="index"),

    #Character URLs
    url(r'^character/$',
            views.character.index, name="char_index"),
    url(r'^character/new/$',
            views.character.char_new, name="char_new"),
    url(r'^character/api_char_list/$',
            views.character.api_char_list, name="char_list"),
    url(r'^character/(?P<char_id>[a-zA-Z0-9_]+)/$',
            views.character.detail, name="char_detail"),
    url(r'^character/(?P<char_id>[a-zA-Z0-9_]+)/level/$',
            views.character.level_up, name="char_level"),
    url(r'^character/(?P<char_id>[a-zA-Z0-9_]+)/api_skill_list/$',
            views.character.api_skill_list, name="char_skills"),


    #Class URLs
    url(r'^class/$',
            views.classes.index, name="class_index"),
    url(r'^class/new/$',
            views.classes.new_class, name="class_new"),
    url(r'^class/api_class_list/$',
            views.classes.api_class_list, name="class_list"),
    url(r'^class/(?P<class_id>[a-zA-Z0-9_]+)/$',
            views.classes.detail, name="class_detail"),

    #Race Views
    url(r'^races/$',
            views.races.index, name="race_index"),
    #Race APIs
    #Feat Veiws
    url(r'^feats/$',
            views.feats.index, name="feat_index"),
    #Feat API
    #Equipment Views
    url(r'^spells/$',
            views.spells.index, name="spell_index")
    #Equipment APIs
)

urlpatterns += staticfiles_urlpatterns()