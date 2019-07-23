from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index),
    url('all.json', views.all_json),
    url('all.html', views.all_html),
    url('find', views.find),
    url('create', views.find)
]