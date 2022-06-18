from django.conf import settings

from .movies import tmdb_movie
from .tv import tmdb_tv
from .search import tmdb_search
from .people import tmdb_people
from .genres import tmdb_genres
from .tvseasons import tmdb_tv_season

__all__ = ['tmdb_movie',
            'tmdb_tv',
            'tmdb_search',
            'tmdb_people',
            'tmdb_genres',
            'tmdb_tv_season']

API_KEY = settings.SECRET_KEY_TMDB
API_VERSION = '3'
REQUESTS_SESSION = None
REQUESTS_TIMEOUT = 300