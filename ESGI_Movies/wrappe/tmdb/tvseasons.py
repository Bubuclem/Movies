from .base import TMDB

class tmdb_tv_season(TMDB):
    BASE_PATH = '/tv/{id}/season'
    URLS = {
    'detail': '/tv/{id}/season/{season}',
    }

    def __init__(self, id=0):
        super(tmdb_tv_season, self).__init__()
        self.id = id

    def detail(self, **kwargs):
        '''
        Détail des saisons.
        '''
        path = self._get_tv_id_season_number_path('detail')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response