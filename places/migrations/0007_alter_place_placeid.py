# Generated by Django 4.2.5 on 2023-09-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_options_remove_place_title_short_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='placeID',
            field=models.SlugField(blank=True, default='', max_length=100, verbose_name='ID места'),
        ),
    ]