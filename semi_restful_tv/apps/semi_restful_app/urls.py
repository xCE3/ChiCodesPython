from django.conf.urls import url
from . import views

urlpatterns = [
    url('shows', views.index),
    url('shows/create', views.create),
    url('shows/new', views.new),
    url('shows/<int:id>', views.show),
    url('shows/<int:id>/edit', views.edit),
    url('shows/<int:id>/destroy', views.destroy),
    url('shows/update', views.update)
]