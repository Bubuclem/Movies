from django.utils.translation import gettext_lazy as _
from django.db import models

class StatusType(models.TextChoices):
        Rumored = 'Rumored', _('Rumeur')
        Planned = 'Planned', _('Planifié')
        InProduction = 'In Production', _('En production')
        PostProduction = 'Post Production', _('Post production')
        Released = 'Released', _('Sorti')
        Canceled = 'Canceled', _('Annulé')
        ReturningSeries = 'Returning Series', _('Série en cours')
        Ended = 'Ended' , _('Terminé')

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name="Genre"
        verbose_name_plural = "Genres"

    def __str__(self) -> str:
        return self.name

class Show(models.Model):
    """
    Show model
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    overview = models.TextField(blank=True)
    homepage = models.CharField(max_length=255, blank=True)
    tagline = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    languages = models.TextField(blank=True)

    first_air_date = models.DateField(blank=True, null=True)
    last_air_date = models.DateField(blank=True, null=True)
    in_production = models.BooleanField(blank=True, null=True)
    status = models.CharField(max_length=255, choices=StatusType.choices, blank=True, null=True)

    popularity = models.FloatField(blank=True)
    vote_count = models.IntegerField(blank=True)
    vote_average = models.FloatField(blank=True)

    number_of_episodes = models.IntegerField(blank=True, null=True)
    number_of_seasons = models.IntegerField(blank=True, null=True)

    poster_path = models.TextField(blank=True,null=True)
    backdrop_path = models.TextField(blank=True, null=True)
    
    original_language = models.CharField(max_length=255, blank=True)
    original_name = models.CharField(max_length=255, blank=True)
    
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.name

    def convert_json_to_object(self, json_show: dict) -> None:
        '''
        Convert json to object
        '''
        self.id = json_show['id']
        self.name = json_show['name']
        self.overview = json_show['overview']
        self.homepage = json_show['homepage']
        self.tagline = json_show['tagline']
        self.type = json_show['type']

        for language in json_show['languages']:
            if self.languages:
                self.languages = '{},{}'.format(str(self.languages), language)
            else:
                self.languages = language

        self.first_air_date = json_show['first_air_date']
        self.last_air_date = json_show['last_air_date']
        self.in_production = json_show['in_production']
        self.status = json_show['status']

        self.popularity = json_show['popularity']
        self.vote_count = json_show['vote_count']
        self.vote_average = json_show['vote_average']

        self.number_of_episodes = json_show['number_of_episodes']
        self.number_of_seasons = json_show['number_of_seasons']

        self.poster_path = json_show['poster_path']
        self.backdrop_path = json_show['backdrop_path']

        self.original_language = json_show['original_language']
        self.original_name = json_show['original_name']

        for genre in json_show['genres']:
            self.save() # Save the show before adding the genre
            self.genres.add(Genre.objects.get(id=genre['id']))

    def get_poster_url(self) -> str:
        '''
        Get url of poster.
        '''
        if self.poster_path:
            return 'https://image.tmdb.org/t/p/w500/{}'.format(self.poster_path)

    def get_percent_average(self) -> int:
        '''
        Return % average of the movie
        '''
        return int(self.vote_average * 10)

    def get_first_genre(self) -> str:
        if self.genres.count() > 0:
            return self.genres.first().name
        else :
            return 'Sans catégorie'

        