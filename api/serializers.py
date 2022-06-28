from rest_framework import serializers

from movies.models import Movie, Genre as MovieGenre
from shows.models import Show, Genre as ShowGenre
from actors.models import Actor

class MovieGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieGenre
        fields = ('id', 'name')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'homepage', 'tagline', 'original_language', 'original_title', 'release_date', 'status', 'adult', 'popularity', 'vote_count', 'vote_average', 'runtime', 'revenue', 'budget', 'video', 'poster_path', 'backdrop_path')

class ShowGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowGenre
        fields = ('id', 'name')

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = ('id', 'name', 'overview', 'homepage', 'tagline', 'type', 'first_air_date', 'last_air_date', 'in_production', 'status', 'popularity', 'vote_count', 'vote_average', 'number_of_episodes', 'number_of_seasons', 'poster_path', 'backdrop_path')

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'biography', 'birthday', 'deathday', 'popularity', 'profile_path', 'adult', 'known_for_department', 'gender', 'also_known_as', 'homepage', 'imdb_id')