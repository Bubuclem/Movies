from .base import TMDB

class tmdb_movie(TMDB):
    BASE_PATH = 'movie'
    URLS = {
        'detail': '/{id}',
        'credits': '/{id}/credits',
        'external_ids': '/{id}/external_ids',
        'images': '/{id}/images',
        'release_dates': '/{id}/release_dates',
        'recommendations' : '/{id}/recommendations',
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
        super(tmdb_movie, self).__init__()
        self.id = id

    def detail(self, **kwargs):
        '''
        Détail d'un film
        '''
        path = self._get_id_path('detail')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def credits(self, **kwargs):
        '''
        Acteurs d'un film
        '''
        path = self._get_id_path('credits')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def external_ids(self, **kwargs):
        '''
        Réseaux sociaux d'un film
        '''
        path = self._get_id_path('external_ids')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(self, **kwargs):
        '''
        Images d'un film
        '''
        path = self._get_id_path('images')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def release_dates(self, **kwargs):
        '''
        Dates de sortie d'un films dans les pays
        '''
        path = self._get_id_path('release_dates')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def recommendations(self, **kwargs):
        '''
        Liste des films recommandés
        '''
        path = self._get_id_path('recommendations')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def reviews(self, **kwargs):
        '''
        Commentaires des utilisateurs
        '''
        path = self._get_id_path('reviews')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def similar_movies(self, **kwargs):
        '''
        Films similaires
        '''
        path = self._get_id_path('similar_movies')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def videos(self, **kwargs):
        '''
        Bandes annonces d'un film
        '''
        path = self._get_id_path('videos')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def watch_providers(self, **kwargs):
        '''
        Plateforme de diffusion d'un film
        '''
        path = self._get_id_path('watch_providers')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def latest(self, **kwargs):
        '''
        Liste des derniers films ajoutés
        '''
        path = self._get_path('latest')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def now_playing(self, **kwargs):
        '''
        Liste des films en salles
        '''
        path = self._get_path('now_playing')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def popular(self, **kwargs):
        '''
        Liste des films populaires
        '''
        path = self._get_path('popular')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def top_rated(self, **kwargs):
        '''
        Liste des films les mieux notés
        '''
        path = self._get_path('top_rated')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def upcoming(self, **kwargs):
        '''
        Liste des prochains films
        '''
        path = self._get_path('upcoming')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response