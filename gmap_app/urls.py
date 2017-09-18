from django.conf.urls import url

from . import views

app_name = 'gmap_app'

urlpatterns = [
    # ex: http://localhost:8000/gmap_app/show_map/
    url(r'^store_addresses/$', views.store_addresses, name='store_addresses'),
    
]

