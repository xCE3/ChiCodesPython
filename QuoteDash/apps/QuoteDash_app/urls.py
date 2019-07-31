from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^quotes$', views.quotes),
    url(r'^create$', views.create),
    url(r'^add_like/(?P<id>\d+)$', views.add_like),
    url(r'^remove_like/(?P<id>\d+)$', views.remove_like),
    url(r'^users/(?P<id>\d+)$', views.show_user)
]