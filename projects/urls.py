from django.conf.urls import url

from . import views
app_name = "projects"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<project_id>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^(?P<project_id>[0-9]+)/complete$', views.details, name='details'),
    url(r'^(?P<project_id>[0-9]+)/team$', views.new_team, name='new_team'),
    url(r'^new_project/$', views.new_project, name='new_project'),
    url(r'^list/$', views.list_projects, name='list'),
    url(r'^logout/$', views.logout_view, name='logout'),
]