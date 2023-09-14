from django.http import Http404, JsonResponse

from conf.wsgi import *
from django.shortcuts import render, get_object_or_404
from places.models import Place, Image

def main(request):
    features = []
    places = Place.objects.prefetch_related('images').all()
    for place in places:
        imgs = []
        for image in place.images.all():
            imgs.append(image.image.url)
        place_details = {
            "title": place.title,
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {
                "lng": place.lon,
                "lat": place.lat,
            },
            "imgs": imgs,
        }
        place_geodata = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat],
            },
            "properties": {
                "title": place.title,
                "placeId": place.placeID,
                "details": place_details,
            }
        }
        features.append(place_geodata)

    places_geojson = {
      "type": "FeatureCollection",
      "features": features,
    }

    return render(request, 'places/index.html', context={'data': places_geojson})


def place_details(request, place_id):
    try:
        place = Place.objects.prefetch_related('images').get(pk=place_id)
    except Place.DoesNotExist:
        raise Http404("No places matches the given query.")
    imgs = []
    for image in place.images.all():
        imgs.append(image.image.url)
    place_details = {
        "title": place.title,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat,
        },
        "imgs": imgs,
    }
    return JsonResponse(place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
