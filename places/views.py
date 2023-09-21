from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def main(request):
    features = []
    places = Place.objects.prefetch_related('images').all()
    for place in places:
        base_url = request.build_absolute_uri()
        path_url = reverse("places", args=(place.pk,))
        place_geodata = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lon, place.lat],
            },
            'properties': {
                'title': place.title,
                'placeId': place.placeID,
                'detailsUrl': f'{base_url}{path_url}',
            },
        }
        features.append(place_geodata)

    places_geojson = {
      'type': 'FeatureCollection',
      'features': features,
    }

    return render(request, 'places/index.html', context={'geo': places_geojson})


def place_details(request, place_id):

    place = get_object_or_404(Place, id=place_id)

    imgs = []
    for image in place.images.all():
        imgs.append(image.image.url)
    place_details = {
        'title': place.title,
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lng': place.lon,
            'lat': place.lat,
        },
        'imgs': [image.image.url for image in place.images.all()],
    }
    return JsonResponse(place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
