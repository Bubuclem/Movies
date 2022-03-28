from .base import TMDB

class Movies(TMDB):
    BASE_PATH = 'movie'
    URLS = {
        'details': '/{id}',
        'credits': '/{id}/credits',
        'external_ids': '/{id}/external_ids',
        'images': '/{id}/images',
        'release_dates': '/{id}/release_dates',
        'reviews': '/{id}/reviews',
        'similar_movies': '/{id}/similar_movies',
        'videos': '/{id}/videos',
        'watch_providers': '/{id}/watch/providers',
        'latest': '/latest',
        'now_playing': '/now_playing',
        'popular': '/popular',
        'top_rated': '/top_rated',
        'upcoming': '/upcoming',
    }

    def __init__(self, id=0):
        super(Movies, self).__init__()
        self.id = id

    def details(self, **kwargs): # Détail du film
        path = self._get_id_path('details')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def credits(self, **kwargs): # Acteurs du film
        path = self._get_id_path('credits')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def external_ids(self, **kwargs): # Réseaux sociaux du film
        path = self._get_id_path('external_ids')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(self, **kwargs): # Images du film
        path = self._get_id_path('images')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def release_dates(self, **kwargs): # Dates de sortie du films dans les pays
        path = self._get_id_path('release_dates')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def reviews(self, **kwargs): # Commentaires des utilisateurs
        path = self._get_id_path('reviews')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def similar_movies(self, **kwargs): # Films similaires
        path = self._get_id_path('similar_movies')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def videos(self, **kwargs): # Vidéos du film
        path = self._get_id_path('videos')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def watch_providers(self, **kwargs): # Plateforme de diffusion du film
        path = self._get_id_path('watch_providers')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def latest(self, **kwargs): # Nouveau films
        path = self._get_path('latest')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def now_playing(self, **kwargs): # Films en salles
        path = self._get_path('now_playing')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def popular(self, **kwargs): # Films populaires
        path = self._get_path('popular')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def top_rated(self, **kwargs): # Films les mieux notés
        path = self._get_path('top_rated')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def upcoming(self, **kwargs): # Prochains films
        path = self._get_path('upcoming')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response