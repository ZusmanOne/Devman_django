from urllib.parse import urlsplit
import requests
from places.models import Place, PlaceImage
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('url_place', type=str)

    def handle(self, *args, **options):
        place_url = options['url_place']
        place_response = requests.get(place_url )
        place_response.raise_for_status()
        serialized_place = place_response.json()
        place, created = Place.objects.get_or_create(
            title=serialized_place['title'],
            defaults={
                'description_short': serialized_place['description_short'],
                'description_long': serialized_place['description_long'],
                'coord_long': serialized_place['coordinates']['lng'],
                'coord_lat': serialized_place['coordinates']['lat'],
            })
        if not created:
            print(f'object {place} already created')
        image_url = serialized_place['imgs']
        for img in image_url:
            if place.images.all():
                break
            image_response = requests.get(img)
            image_response.raise_for_status()
            urlsplit_image = urlsplit(img)
            image_name = urlsplit_image.path.split('/')[-1]
            image, created = PlaceImage.objects.get_or_create(
                place=place,
                image=ImageFile(ContentFile(image_response.content), name=image_name),
            )
