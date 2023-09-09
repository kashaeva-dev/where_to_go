from conf.wsgi import *
from django.shortcuts import render
from places.models import Place, Image

def main(request):
    data = {'hello': 'word'}
    data1 = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": "{% static 'places/moscow_legends.json' %}"
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": "{% static 'places/roofs24.json' %}"
          }
        }
      ]
    }
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
                "title":place.title_short,
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


def main2(request):
    data = {'hello': 'word'}
    return render(request, 'places/test.html', context={'data': data})
