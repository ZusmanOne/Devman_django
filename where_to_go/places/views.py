from .models import Place
from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse


def index(request):
    places = Place.objects.all()
    serialized_places = []
    for place in places:
        serialized_places.append(
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.coord_long, place.coord_lat]
                    },
                    "properties": {
                        "title": place.title,
                        "placeId": place.pk,
                        "detailsUrl": reverse('place_detail', args=[place.pk])
                    }
                }
        )
    content_places = {
            "type": "FeatureCollection",
            "features": serialized_places
        }
    context = {'places': content_places}
    return render(request, 'index.html', context)


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    serialized_place = {
        'title': place.title,
        'imgs': [img.image.url for img in place.image.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {'lat': place.coord_lat,
                        'lng': place.coord_long}
    }

    return JsonResponse(serialized_place, json_dumps_params={'ensure_ascii': False, 'indent': 4})
