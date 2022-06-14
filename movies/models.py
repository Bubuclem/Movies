from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.db import models

class StatusType(models.TextChoices):
        Rumored = 'Rumored', _('Rumeur')
        Planned = 'Planned', _('Planifié')
        InProduction = 'In Production', _('En production')
        PostProduction = 'Post Production', _('Post production')
        Released = 'Released', _('Sorti')
        Canceled = 'Canceled' , _('Annulé')

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name="Genre"
        verbose_name_plural = "Genres"

    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    '''
    Class : Movie
    Description : Model of the movie
    '''
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True)
    homepage = models.CharField(max_length=255, blank=True)
    tagline = models.CharField(max_length=255, blank=True)
    
    original_language = models.CharField(max_length=255, blank=True)
    original_title = models.CharField(max_length=255, blank=True)

    release_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, choices=StatusType.choices, blank=True, null=True)

    adult = models.BooleanField(blank=True)

    popularity = models.FloatField(blank=True)
    vote_count = models.IntegerField(blank=True)
    vote_average = models.FloatField(blank=True)

    runtime = models.IntegerField(blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    video = models.BooleanField(null=True)

    poster_path = models.TextField(blank=True, null=True)
    backdrop_path = models.TextField(blank=True, null=True)
    
    genres = models.ManyToManyField(Genre, blank=True)
    
    def __str__(self):
        return self.title

    def convert_json_to_object(self, json_movie: dict) -> None:
        '''
        Convert json to object
        '''
        self.id = json_movie['id']

        self.title = json_movie['title']
        self.overview = json_movie['overview']

        if json_movie['release_date']:
            self.release_date = datetime.strptime(json_movie['release_date'], "%Y-%m-%d").date()

        self.status = json_movie['status']
        self.adult = json_movie['adult']
        self.popularity = json_movie['popularity']
        self.vote_count = json_movie['vote_count']
        self.vote_average = json_movie['vote_average']
        self.original_language = json_movie['original_language']
        self.original_title = json_movie['original_title']
        self.runtime = json_movie['runtime']
        self.revenue = json_movie['revenue']
        self.budget = json_movie['budget']
        self.homepage = json_movie['homepage']
        self.tagline = json_movie['tagline']
        self.video = json_movie['video']

        self.poster_path = json_movie['poster_path']
        self.backdrop_path = json_movie['backdrop_path']

        for genre in json_movie['genres']:
            self.save() # On enregistre le film avant de lui assigner un genre
            self.genres.add(Genre.objects.get(id=genre['id']))

    def get_poster_url(self) -> str:
        '''
        Get url of poster.
        '''
        if self.poster_path:
            return 'https://image.tmdb.org/t/p/w500/{}'.format(self.poster_path)
    
    def get_first_genre(self) -> str:
        '''
        Return the first genre of the movie
        '''
        if self.genres.count() > 0:
            return self.genres.first().name
        else:
            return 'Sans catégorie'

    def get_percent_average(self) -> int:
        '''
        Return % average of the movie
        '''
        return int(self.vote_average * 10)

    def get_runtime(self) -> str:
        '''
        Return minutes of the movie
        Convert runtime from minutes to hours and minutes
        '''
        if self.runtime:
            return str(self.runtime // 60) + 'h ' + str(self.runtime % 60) + 'min'