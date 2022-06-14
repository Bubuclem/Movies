# Generated by Django 4.0.4 on 2022-06-01 21:25

import ESGI_Movies.wrappe.tmdb.tv
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('overview', models.TextField(blank=True)),
                ('poster_path', models.TextField(blank=True)),
                ('backdrop_path', models.TextField(blank=True)),
                ('first_air_date', models.TextField(blank=True)),
                ('last_air_date', models.TextField(blank=True)),
                ('number_of_episodes', models.IntegerField(blank=True)),
                ('number_of_seasons', models.IntegerField(blank=True)),
                ('popularity', models.FloatField(blank=True)),
                ('vote_count', models.IntegerField(blank=True)),
                ('vote_average', models.FloatField(blank=True)),
                ('adult', models.BooleanField(blank=True)),
                ('original_language', models.CharField(blank=True, max_length=255)),
                ('original_name', models.CharField(blank=True, max_length=255)),
                ('genre_ids', models.TextField(blank=True)),
                ('genres', models.TextField(blank=True)),
            ],
            bases=(ESGI_Movies.wrappe.tmdb.tv.tmdb_tv, models.Model),
        ),
    ]