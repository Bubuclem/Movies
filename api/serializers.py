from django.contrib.auth.models import User, Group
from rest_framework import serializers

from ESGI_Movies.wrappe.tmdb import tmdb_movie

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tmdb_movie
        fields = ['__all__']