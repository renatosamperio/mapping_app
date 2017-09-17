from django.forms import ModelForm
from gmap_app.models import Places

class PlacesForm(ModelForm):
  class Meta:
      model = Places
      fields = ('address', 'latitude', 'longitude',)
