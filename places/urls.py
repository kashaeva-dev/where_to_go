from django.urls import path

from places import views

urlpatterns = [
    path('', views.main, name='main'),
]
