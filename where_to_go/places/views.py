from .models import *
from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse


def index(request):
    places = Place.objects.all()
    places_list = []
    for i in places:
        places_list.append(
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [i.coord_long, i.coord_lat]
                    },
                    "properties": {
                        "title": i.title,
                        "placeId": i.pk,
                        "detailsUrl": reverse('place_detail', args=[i.pk])
                    }
                }
        )
    places_json = {
            "type": "FeatureCollection",
            "features": places_list
        }
    context = {'places': places_json}
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


