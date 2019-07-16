from django.conf.urls import url
from . import views

urlpatterns = [
    url('shows', views.index),
    url('create', views.create),
    url('new', views.new),
    url(r'^(?P<id>\d+)$', views.show),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^(?P<id>\d+)/destroy$', views.destroy),
    url('update', views.update)
]

