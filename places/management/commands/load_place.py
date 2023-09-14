import itertools

import requests
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from places.models import Place


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'place_url',
            type=str,
            help='Ссылка на информацию о локации',
        )


    def handle(self, *args, **options):
        url = options['place_url']

        response = requests.get(url)
        response.raise_for_status()

        place = response.json()

        def generate_slug(text):
            slug_candidate = slug_original = slugify(text, allow_unicode=True)
            for i in itertools.count(1):
                if not Place.objects.filter(slug=slug_candidate).exists():
                    break
                slug_candidate = '{}-{}'.format(slug_original, i)

            return slug_candidate

        try:
            new_place, _ = Place.objects.get_or_create(
                title = place['title'],
                defaults={
                    'placeID': generate_slug(place['title']),
                    'description_short': place['description_short'],
                    'description_long': place['description_long'],
                    'lat': place['coordinates']['lat'],
                    'lon': place['ccoordinates']['lng'],
                }
            )
        except:
            pass

