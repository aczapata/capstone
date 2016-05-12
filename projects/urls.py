from django.conf.urls import url
from url_obfuscate.helpers import generate_url_pattern
from . import views
app_name = "projects"

"""
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(generate_url_pattern('obfuscated_link',params=['(?P<project_id>[0-9]+)']), views.obfuscated_link, name='obfuscated_link'),
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<project_id>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^(?P<project_id>[0-9]+)/complete$', views.details, name='details'),
    url(r'^(?P<project_id>[0-9]+)/team$', views.new_team, name='new_team'),
    url(r'^new_project/$', views.new_project, name='new_project'),
    url(r'^list/$', views.list_projects, name='list'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
"""
urlpatterns = [
    url(r'^$', views.index, name='index'),    
    url(r'^new_project', views.new_project, name='new_project'),
    url(r'^list', views.list_projects, name='list'),
    url(r'^(?P<project_id>[^/]+)/team$', views.new_team, name='new_team'),
    url(r'^project/(?P<project_id>[^/]+)/$', views.detail, name='detail'),
    url(r'^project/(?P<project_id>[^/]+)/complete$', views.details, name='details'),
    url(r'^project/(?P<project_id>[^/]+)/edit$', views.edit, name='edit'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
