from django.utils.translation import gettext_lazy as _
from django.db import models
from management.models import SpokenLanguage

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

class LastEpisode(models.Model):
    '''
    Dernier épisode de la série
    '''
    air_date = models.DateField()
    season_number = models.IntegerField()
    episode_number = models.IntegerField()
    name = models.CharField(max_length=255)
    overview = models.TextField()
    production_code = models.CharField(max_length=255)
    still_path = models.CharField(max_length=255,blank=True,null=True)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Season(models.Model):
    '''
    Saison de la série
    '''
    id = models.IntegerField(primary_key=True)
    air_date = models.DateField(blank=True,null=True)
    episode_count = models.IntegerField()
    season_number = models.IntegerField()
    name = models.CharField(max_length=255)
    overview = models.TextField()
    poster_path = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self) -> str:
        return self.name

    def get_poster_url(self):
        if self.poster_path is not None:
            return 'https://image.tmdb.org/t/p/w500{}'.format(self.poster_path)

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
    languages = models.ManyToManyField(SpokenLanguage, blank=True)

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
    
    last_episode = models.OneToOneField(LastEpisode, on_delete=models.CASCADE, blank=True, null=True)
    seasons = models.ManyToManyField(Season, blank=True)

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

        self.last_episode = LastEpisode.objects.create(
            air_date=json_show['last_episode_to_air']['air_date'],
            season_number=json_show['last_episode_to_air']['season_number'],
            episode_number=json_show['last_episode_to_air']['episode_number'],
            name=json_show['last_episode_to_air']['name'],
            overview=json_show['last_episode_to_air']['overview'],
            production_code=json_show['last_episode_to_air']['production_code'],
            still_path=json_show['last_episode_to_air']['still_path'],
            vote_average=json_show['last_episode_to_air']['vote_average'],
            vote_count=json_show['last_episode_to_air']['vote_count']
        )

        for season in json_show['seasons']:
            self.save() # Save show before adding seasons

            try:
                _season = Season.objects.get(id=season['id'])
            except Season.DoesNotExist:
                _season = Season.objects.create(
                id=season['id'],
                air_date=season['air_date'],
                episode_count=season['episode_count'],
                season_number=season['season_number'],
                name=season['name'],
                overview=season['overview'],
                poster_path=season['poster_path']
                )

            self.seasons.add(_season)

        for language in json_show['spoken_languages']:
            self.save() # Save the show before adding the genre
            
            try :
                _language = SpokenLanguage.objects.get(iso_639_1=language['iso_639_1'])
            except SpokenLanguage.DoesNotExist:
                _language = SpokenLanguage.objects.create(iso_639_1=language['iso_639_1'], name=language['name'])
                _language.save()

            
            self.languages.add(_language)

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

        