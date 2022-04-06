from .models import *
from django.shortcuts import render


def index(request):
  places = Place.objects.all()
  my_place = []
  for i in places:
    my_place.append({
      "type": "FeatureCollection",
      "features":[
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [i.coord_long, i.coord_lat]
          },
          "properties": {
            "title": i.title,
            "placeId": i.pk,
            "detailsUrl": "#"
          }
        }
      ]

    })

  #
  # my_place = {
  #   "type": "FeatureCollection",
  #   "features": [
  #     {
  #       "type": "Feature",
  #       "geometry": {
  #         "type": "Point",
  #         "coordinates": [37.62, 55.793676]
  #       },
  #       "properties": {
  #         "title": "«Легенды Москвы",
  #         "placeId": "moscow_legends",
  #         "detailsUrl": "/static/where-to-go-frontend/places/moscow_legends.json"
  #       }
  #     },
  #     {
  #       "type": "Feature",
  #       "geometry": {
  #         "type": "Point",
  #         "coordinates": [37.64, 55.753676]
  #       },
  #       "properties": {
  #         "title": "Крыши24.рф",
  #         "placeId": "roofs24",
  #         "detailsUrl": "/static/where-to-go-frontend/places/roofs24.json"
  #       }
  #     }
  #   ]
  # }
  context = {'places': my_place}
  return render(request, 'index.html', context)

# Create your views here.
