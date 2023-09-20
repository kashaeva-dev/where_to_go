from django.http import Http404, JsonResponse
from django.shortcuts import render

from places.models import Place


def main(request):
    features = []
    places = Place.objects.prefetch_related('images').all()
    for place in places:
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
            'imgs': imgs,
        }
        place_geodata = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lon, place.lat],
            },
            'properties': {
                'title': place.title,
                'placeId': place.placeID,
                'details': place_details,
            },
        }
        features.append(place_geodata)

    places_geojson = {
      'type': 'FeatureCollection',
      'features': features,
    }

    return render(request, 'places/index.html', context={'data': places_geojson})


def place_details(request, place_id):
    try:
        place = Place.objects.prefetch_related('images').get(pk=place_id)
    except Place.DoesNotExist:
        raise Http404('No places matches the given query.')
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
        'imgs': imgs,
    }
    return JsonResponse(place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
