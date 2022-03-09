from rest_framework import serializers
from django.conf import settings

import tmdbsimple as tmdb
import requests

class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tmdb.Movies
        fields = ['id', 'title']

    def create(self):
        tmdb.API_KEY = settings.SECRET_KEY_TMDB
        tmdb.REQUESTS_SESSION = requests.Session()
        return tmdb