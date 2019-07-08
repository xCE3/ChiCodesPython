from django.conf.urls import url
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
        url(r'^$', views.index),                        # would only match localhost:8000/bears
        url(r'^new$', views.new),
        url(r'^create$', views.create),
        url(r'^15/(?P<my_val>\d+)$', views.show),    # would match localhost:8000/15/15    
        url(r'^edit/(?P<id>[0-9]+)$', views.edit),    # would match localhost:8000/edit/9/
    	url(r'^delete(?P<id>[0-9]+)/delete$', views.destroy),  # would match localhost:8000/17/brown
]