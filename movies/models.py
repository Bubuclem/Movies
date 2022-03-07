from urllib import response
import requests
from enum import Enum
from django.db import models

from django.conf import settings

class type_media(Enum):
    Movie = 1
    TV = 2

class BaseTMDB():
    URL = 'https://api.themoviedb.org/3'
    api_key = settings.SECRET_KEY_TMDB
    enum_type = type_media.Movie
    type = None

    def __init__(self,enum_type) -> None:
        self.enum_type = enum_type
        self.type = 'movie'
        if self.type == 2:
            self.type = 'tv'

    def __url_replace(self,url) -> str:
        return url.replace(" ","%20")

    def __url_request(self,url):
        return requests.get(url,headers={'content-type': 'application/json'})

class Video(models.Model):
    id = models.IntegerField(primary_key=True)

class People(models.Model):
    id = models.IntegerField(primary_key=True)

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)

class Media(models.Model,BaseTMDB):
    id                  = models.IntegerField(primary_key=True)
    overview            = models.CharField(max_length=200)
    poster_path         = models.CharField(max_length=200)
    popularity          = models.FloatField(max_length=200)
    backdrop_path       = models.CharField(max_length=200)
    vote_average        = models.FloatField()
    release_date        = models.CharField(max_length=200)
    original_language   = models.CharField(max_length=200)
    genre_ids           = models.JSONField(max_length=200)
    vote_count          = models.IntegerField()
    title               = models.CharField(max_length=200)
    original_title      = models.CharField(max_length=200)
    origin_country      = models.JSONField()
    video               = models.BooleanField()
    adult               = models.BooleanField()

    budget              = models.IntegerField()
    revenue             = models.IntegerField()
    runtime             = models.IntegerField()
    status              = models.CharField(max_length=200)
    tagline             = models.CharField(max_length=200)

    def __init__(self,json) -> None:
        self.id                 = json.get('id')
        self.overview           = json.get('overview')
        self.poster_path        = json.get('poster_path')
        self.popularity         = json.get('popularity')
        self.backdrop_path      = json.get('backdrop_path')
        self.vote_average       = json.get('vote_average')
        self.release_date       = json.get('release_date')
        self.original_language  = json.get('original_language')
        self.genre_ids          = json.get('genre_ids')
        self.vote_count         = json.get('vote_count')
        self.title              = json.get('title')
        self.original_title     = json.get('original_title')

    def get_detail(self,id):
        response = self.__url_request('{}/{}/{}?api_key={}&language=fr'.format(self.URL,self.type,id,self.api_key))
        media = Media(response)
        return media

    def get_account_states(self,id):
        return '{}/{}/{}/account_states?api_key={}'.format(self.URL,self.type,id,self.api_key)
    def alternative_titles(self,id,country=""):
        return '{}/{}/{}/alternative_titles?api_key={}'.format(self.URL,self.type,id,self.api_key)