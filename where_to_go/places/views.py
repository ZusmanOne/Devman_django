import json
from django.core.files.base import File, ContentFile
from django.core.files.images import ImageFile
from .models import *
from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse
import requests
from io import BytesIO
from urllib.parse import urlsplit

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


def load_place():
    url = 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%92%D0%BE%D0%B4%D0%BE%D0%BF%D0%B0%D0%B4%20%D0%A0%D0%B0%D0%B4%D1%83%D0%B6%D0%BD%D1%8B%D0%B9.json'
    response = requests.get(url)
    json_obj = json.loads(response.content)
    url_image = json_obj['imgs']
    #response_image = requests.get(url_image)
    # image_content = Image.open(BytesIO(response_image.content))
    # print(image_content)
    my_place, created = Place.objects.get_or_create(
        title = json_obj['title'],
        description_short=json_obj['description_short'],
        description_long=json_obj['description_long'],
        coord_long=json_obj['coordinates']['lng'],
        coord_lat=json_obj['coordinates']['lat'],

    )
    for my_image in url_image:
        response_image = requests.get(my_image)
        image_urlsplit = urlsplit(my_image)
        image_name = image_urlsplit.path.split('/')[-1]
        img, created = Image.objects.get_or_create(
            place=my_place,
            image=ImageFile(ContentFile(response_image.content),name=image_name),
    )

    #my_place.image.add(image=ImageFile(ContentFile(response_image.content),name='123.jpg'))

    # my_place.image.save(json_obj['imgs'],save=True)
    # my_place.save()
    # print(json_obj['coordinates']['lng'],json_obj['coordinates']['lat'])



load_place()
