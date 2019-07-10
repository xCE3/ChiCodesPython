from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url('generate', views.generate),
    url('reset', views.reset)
]