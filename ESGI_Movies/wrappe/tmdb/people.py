from .base import TMDB

class tmdb_people(TMDB):
    BASE_PATH = 'person'
    URLS = {
        'detail': '/{id}',
        'movie_credits': '/{id}/movie_credits',
        'tv_credits': '/{id}/tv_credits',
        'combined_credits': '/{id}/combined_credits',
        'external_ids': '/{id}/external_ids',
        'images': '/{id}/images',
        'latest': '/latest',
        'popular': '/popular',
    }

    def __init__(self, id=0):
        super(tmdb_people, self).__init__()
        self.id = id

    def detail(self, **kwargs): # Fiche d'un acteur
        path = self._get_id_path('detail')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response
    
    def movie_credits(self, **kwargs): # Films de l'acteur
        path = self._get_id_path('movie_credits')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def tv_credits(self, **kwargs): # Séries de l'acteur
        path = self._get_id_path('tv_credits')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def combined_credits(self, **kwargs): # Séries et films
        path = self._get_id_path('combined_credits')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def external_ids(self, **kwargs): # Réseaux sociaux
        path = self._get_id_path('external_ids')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(self, **kwargs): # Photos
        path = self._get_id_path('images')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def latest(self, **kwargs):  # Acteurs récemment ajoutés
        path = self._get_path('latest')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def popular(self, **kwargs): # Acteurs populaires
        path = self._get_path('popular')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response