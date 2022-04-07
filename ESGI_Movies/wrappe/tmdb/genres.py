from .base import TMDB

class tmdb_genres(TMDB):
    BASE_PATH = 'genre'
    URLS = {
        'movie_list': '/movie/list',
        'tv_list': '/tv/list',
    }

    def __init__(self, id=0):
        super(tmdb_genres, self).__init__()
        self.id = id

    def movie_list(self, **kwargs): # Liste des genres des films
        path = self._get_path('movie_list')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def tv_list(self, **kwargs): # Liste des genres des séries
        path = self._get_path('tv_list')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response