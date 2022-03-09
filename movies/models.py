import requests
from enum import Enum
from django.db import models

import tmdbsimple as tmdb
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
    pass

class People(models.Model):
    pass

class Genre(models.Model):
    pass

class Media(models.Model):
    pass
