from .models import *
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


def index(request):
    places = Place.objects.all()
    places_list = []
    for i in places:
        places_list.append({
            "type": "FeatureCollection",
            "features": [
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
    context = {'places': places_list}
    return render(request, 'index.html', context)


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_list = {
        'title': place.title,
        'imgs': [img.image.url for img in place.image.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {'lat': place.coord_lat,
                        'lng': place.coord_long}
    }
    return JsonResponse(place_list, json_dumps_params={'ensure_ascii': False, 'indent': 4})



