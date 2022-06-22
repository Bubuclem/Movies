from datetime import datetime
from django.db import models

class Actor(models.Model):
    """
    Actor model
    """
    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    deathday = models.DateField(blank=True, null=True)
    known_for_department = models.CharField(max_length=255, blank=True, null=True)
    adult = models.BooleanField(blank=True)
    gender = models.IntegerField(null=True)
    profile_path = models.TextField(blank=True, null=True)
    also_known_as = models.TextField(blank=True, null=True)

    popularity = models.FloatField(blank=True)
    homepage = models.TextField(blank=True, null=True)
    imdb_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def convert_json_to_object(self, json_actor: dict) -> None:
        '''
        Convert json to object
        '''
        self.id = json_actor['id']
        self.name = json_actor['name']
        self.biography = json_actor['biography']

        if json_actor['birthday']:
            self.birthday = datetime.strptime(json_actor['birthday'], "%Y-%m-%d").date()
        if json_actor['deathday']:
            self.deathday = datetime.strptime(json_actor['deathday'], "%Y-%m-%d").date()

        self.known_for_department = json_actor['known_for_department']
        self.adult = json_actor['adult']
        self.gender = json_actor['gender']
        self.profile_path = json_actor['profile_path']

        for also_known_as in json_actor['also_known_as']:
            if self.also_known_as:
                self.also_known_as = '{},{}'.format(str(self.also_known_as), also_known_as)
            else:
                self.also_known_as = also_known_as

        self.popularity = json_actor['popularity']
        self.homepage = json_actor['homepage']
        self.imdb_id = json_actor['imdb_id']

    
    def get_profile_path(self):
        '''
        Get url for profile_path
        '''
        if self.profile_path:
            return 'https://image.tmdb.org/t/p/w500{}'.format(self.profile_path)