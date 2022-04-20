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
        url_place = options['url_place']
        response_place = requests.get(url_place)
        response_place.raise_for_status()
        json_place = response_place.json()
        new_place, created = Place.objects.get_or_create(
            title=json_place['title'],
            defaults={
                'description_short': json_place['description_short'],
                'description_long': json_place['description_long'],
                'coord_long': json_place['coordinates']['lng'],
                'coord_lat': json_place['coordinates']['lat'],
            })
        if not created:
            print(f'object {new_place} already created')
        image_url = json_place['imgs']
        if not new_place.image.all():
            for img in image_url:
                response_image = requests.get(img)
                response_image.raise_for_status()
                urlsplit_image = urlsplit(img)
                image_name = urlsplit_image.path.split('/')[-1]
                new_image, created = PlaceImage.objects.get_or_create(
                    place=new_place,
                    image=ImageFile(ContentFile(response_image.content), name=image_name),
                )
