from .base import TMDB

class tmdb_search(TMDB):
    BASE_PATH = 'search'
    URLS = {
        'multi': '/multi',
        'movie': '/movie',
        'show': '/tv',
        'person': '/person'
    }

    def multi(self, **kwargs):
        """
        Recherche dans tout les types, films, series, acteurs
        """
        path = self._get_path('multi')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def movie(self, **kwargs):
        """
        Recherche les films en rapport avec la recherche
        """
        path = self._get_path('movie')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def show(self, **kwargs):
        """
        Recherche les séries en rapport avec la recherche
        """
        path = self._get_path('show')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def person(self, **kwargs):
        """
        Recherche les acteurs en rapport avec la recherche
        """
        path = self._get_path('person')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response