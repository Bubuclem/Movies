import os
import requests

from django.conf import settings

from .movies import Movies
from .tv import TV
from .search import Search

__all__ = ['Movies',
            'TV',
            'Search']

API_KEY = settings.SECRET_KEY_TMDB
API_VERSION = '3'
REQUESTS_SESSION = None
REQUESTS_TIMEOUT = 300