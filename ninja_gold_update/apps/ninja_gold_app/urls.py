from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url('process_money', views.process),
    url('reset', views.reset)
]