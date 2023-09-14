import itertools

from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Название места',
                             unique=True,
                             )
    placeID = models.SlugField(max_length=100, verbose_name='ID места', default='', blank=True)
    description_short = models.TextField(verbose_name='Краткое описание', blank=True)
    description_long = HTMLField(verbose_name='Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.title

    def _generate_slug(self):
        max_length = self._meta.get_field('placeID').max_length
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Place.objects.filter(placeID=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.placeID = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Место')
    image = models.ImageField(upload_to='place_images', verbose_name='Изображение')
    image_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering=['image_order']

    def __str__(self):
        return f"{self.pk} {self.place.title}"
