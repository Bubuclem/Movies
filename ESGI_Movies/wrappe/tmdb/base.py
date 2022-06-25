import json
import requests

class APIKeyError(Exception):
    pass

class TMDB(object):
    # Entête de notre requête de type Json
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Connection': 'close'}
    BASE_PATH = '' # Lien vers tmdb
    URLS = {}

    def __init__(self):
        from . import API_VERSION, REQUESTS_SESSION, REQUESTS_TIMEOUT
        self.base_uri = 'https://api.themoviedb.org'
        self.base_uri += '/{version}'.format(version=API_VERSION)
        self.session = REQUESTS_SESSION
        self.timeout = REQUESTS_TIMEOUT
    
    def _get_path(self, key):
        return self.BASE_PATH + self.URLS[key]

    def _get_id_path(self, key):
        return self._get_path(key).format(id=self.id)

    def _get_tv_id_season_number_path(self, key):
        return self._get_path(key).format(id=self.id, season_number=self.season_number)

    def _get_complete_url(self, path):
        return '{base_uri}/{path}'.format(base_uri=self.base_uri, path=path)

    def _get_params(self, params):
        from . import API_KEY
        if not API_KEY:
            raise APIKeyError

        api_dict = {'api_key': API_KEY}
        if params:
            params.update(api_dict)
            for key, value in params.items():
                if isinstance(params[key], bool):
                    params[key] = 'true' if value is True else 'false'

        else:
            params = api_dict
        return params

    def _request(self, method, path, params=None, payload=None):
        url = self._get_complete_url(path)
        params = self._get_params(params)

        if self.session is None:
            response = requests.request(
                method,
                url,
                params=params,
                data=json.dumps(payload) if payload else payload,
                headers=self.headers, timeout=self.timeout
            )

        else:
            response = self.session.request(
                method,
                url,
                params=params,
                data=json.dumps(payload) if payload else payload,
                headers=self.headers, timeout=self.timeout
            )

        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.json()

    def _GET(self, path, params=None):
        return self._request('GET', path, params=params)

    def _set_attrs_to_values(self, response={}):
        if isinstance(response, dict):
            for key in response.keys():
                if not hasattr(self, key) or not callable(getattr(self, key)):
                    setattr(self, key, response[key])