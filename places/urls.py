from django.urls import path

from places import views

urlpatterns = [
    path('', views.main, name='main'),
    path('places/<int:place_id>/', views.place_details, name='places'),
]
