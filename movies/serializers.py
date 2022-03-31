from rest_framework import serializers
from django.conf import settings

from .models import Movie, Show

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id', 'title', 'poster_path', 'overview', 'release_date', 'original_title', 'original_language', 'backdrop_path', 'popularity', 'vote_count', 'vote_average', 'adult']

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = ['tv_id', 'name', 'poster_path', 'overview', 'original_name', 'original_language', 'backdrop_path', 'popularity', 'vote_count', 'vote_average']