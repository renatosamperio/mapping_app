from django.conf.urls import url

from . import views

app_name = 'gmap_app'

urlpatterns = [
    # ex: http://localhost:8000/gmap_app/show_map/
    url(r'^show_map/$', views.show_map, name='show_map'),
    
]

