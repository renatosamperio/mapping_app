import textwrap
import pprint

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import View

from gmap_app.forms import PlacesForm
from gmap_app.models import Places

def remove_all_places():
  ''' Removes all places from stored models'''
  existing_items = Places.objects.all()
  print(" Removing [%d] existing items"%len(existing_items))
  for item in existing_items:
    item.delete()

def address_is_distinct():
  existing_items = Places.objects.all()
  print(" Removing existing duplicated addresses")
  for address in Places.objects.values_list('address', flat=True).distinct():
    Places.objects.filter(pk__in=Places.objects.filter(address=address).values_list('id', flat=True)[1:]).delete()

def store_addresses(request):
    
    ## The first time the page is loaded or whenever is reloaded via browser
    ##   it will remove all items
    if request.method == 'GET':
      remove_all_places()
    elif request.method == 'POST':
      ## Preparing data dynamically for store in model
      print(" Parsing URL encoded data from POST method")
      modelsPlaces = ['address', 'latitude', 'longitude']
      postDict = request.POST.dict()
      postKeys = postDict.keys()
      placesDict = {}
      
      ## Parsing URL encoded data for storing one-by-one
      for modelKey in modelsPlaces:
        for key in postKeys:
          if key.startswith(modelKey):
            item = postDict[key]
            item_id = key[len(modelKey):]
            item_id_exist = item_id in placesDict.keys()
            if item_id not in placesDict.keys():
              placesDict[item_id]={}
            placesDict[item_id].update({modelKey:item})

      ## Store any places found from URL encoded
      if len(placesDict)>0:
        placesDictKeys = placesDict.keys()
        print(" Found [%d] elements after submit"%len(placesDictKeys))
        for _id in placesDictKeys:
          form = PlacesForm(placesDict[_id])
          if form.is_valid():
            print("  Creating model forms for item ID [%s]"%_id)
            form.save()

      address_is_distinct()
    return render(request, 'gmap_app/map.html')