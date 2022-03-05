from enum import Enum
from django.db import models

from django.conf import settings

class type_media(Enum):
    Movie = 1
    TV = 2

class BaseTMDB():
    url_base = 'https://api.themoviedb.org/3'
    api_key = settings.SECRET_KEY_TMDB
    enum_type = type_media.Movie
    type = None

    def __init__(self,enum_type) -> None:
        self.enum_type = enum_type 
        match enum_type:
            case 1:
                self.type='movie'
            case 2:
                self.type='tv'

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

    def get_detail(self,id):
        return '{}/{}/{}?api_key={}&language=fr'.format(self.url_base,self.type,id,self.api_key)
    def get_account_states(self,id):
        return '{}/{}/{}/account_states?api_key={}'.format(self.url_base,self.type,id,self.api_key)
    def alternative_titles(self,id,country=""):
        return '{}/{}/{}/alternative_titles?api_key={}'.format(self.url_base,self.type,id,self.api_key)