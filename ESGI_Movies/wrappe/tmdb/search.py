from .base import TMDB

class tmdb_search(TMDB):
    BASE_PATH = 'search'
    URLS = {
        'multi': '/multi',
    }

    def multi(self, **kwargs): # Recherche dans tout les types, films, series, acteurs
        path = self._get_path('multi')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response