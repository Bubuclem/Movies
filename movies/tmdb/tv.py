from .base import TMDB

class TV(TMDB):
    BASE_PATH = 'tv'
    URLS = {
        'detail': '/{id}',
        'credits': '/{id}/credits',
        'episode_groups': '/{id}/episode_groups',
        'external_ids': '/{id}/external_ids',
        'images': '/{id}/images',
        'reviews': '/{id}/reviews',
        'similar': '/{id}/similar',
        'videos': '/{id}/videos',
        'watch_providers': '/{id}/watch/providers',
        'latest': '/latest',
        'on_the_air': '/on_the_air',
        'popular': '/popular',
        'top_rated': '/top_rated',
    }

    def __init__(self, id=0):
        super(TV, self).__init__()
        self.id = id

    def info(self, **kwargs): # Détail de la série
        path = self._get_tv_id_season_number_path('info')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def credits(self, **kwargs): # Acteurs du film
        path = self._get_id_path('credits')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def episode_groups(self, **kwargs): # Liste des episodes par saisons
        path = self._get_id_path('episode_groups')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def external_ids(self, **kwargs): # Réseaux sociaux
        path = self._get_id_path('external_ids')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(self, **kwargs): # Images de la série
        path = self._get_id_path('images')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def reviews(self, **kwargs): # Commentaires des utilisateurs
        path = self._get_id_path('reviews')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def similar(self, **kwargs): # Séries similaires
        path = self._get_id_path('similar')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return 

    def videos(self, **kwargs): # Bandes annonces de la série
        path = self._get_id_path('videos')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def watch_providers(self, **kwargs):
        path = self._get_id_path('watch_providers')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)

    def latest(self, **kwargs): # Nouvelles séries
        path = self._get_id_path('latest')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def on_the_air(self, **kwargs): # Séries en cours de diffusion
        path = self._get_path('on_the_air')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def popular(self, **kwargs): # Séries populaires
        path = self._get_path('popular')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def top_rated(self, **kwargs): # Séries les mieux notées
        path = self._get_path('top_rated')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response