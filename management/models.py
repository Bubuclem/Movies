from ast import arg
from cgitb import enable
import datetime
from email.mime import application

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class MediaType(models.TextChoices):
        Movie = 'movie',
        Show = 'show',
        Both = 'both'

class SpokenLanguage(models.Model):
    iso_639_1 = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Language parlé"
        verbose_name_plural = "Languages parlés"

    def __str__(self):
        return self.name

class Watched(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    media_id = models.IntegerField()
    media_type = models.CharField(max_length=5,choices=MediaType.choices,default=MediaType.Movie)
    pub_date = models.DateTimeField('date published',auto_now=True)

    class Meta:
        verbose_name = "Visionnage"
        verbose_name_plural = "Visionnés"

    def __str__(self) -> str:
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Favorite(models.Model):
    '''
    Media favorite by user
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    media_id = models.IntegerField()
    media_type = models.CharField(max_length=5,choices=MediaType.choices,default=MediaType.Movie)
    pub_date = models.DateTimeField('date published',auto_now=True)

    class Meta:
        verbose_name = "Favori"
        verbose_name_plural = "Favoris"

    def __str__(self) -> str:
        return self.name

class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    content = models.CharField(max_length=1000)
    media_id = models.IntegerField()
    media_type = models.CharField(max_length=5,choices=MediaType.choices,default=MediaType.Movie)
    pub_date = models.DateTimeField('date published',auto_now=True)

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self) -> str:
        return self.content

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def author(self) -> str:
        return self.user.username

    def created_at(self) -> str:
        return self.pub_date

class Cast(models.Model):
    '''
    Class cast for movies and tv shows.
    '''
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    known_for_department = models.CharField(max_length=255)
    adult = models.BooleanField(blank=True,null=True)
    gender = models.IntegerField()
    original_name = models.CharField(max_length=255)
    popularity = models.FloatField(blank=True)
    profile_path = models.TextField(blank=True, null=True)
    credit_id = models.CharField(max_length=255)
    character = models.CharField(max_length=255)
    cast_id = models.IntegerField(blank=True)
    order = models.IntegerField(blank=True)

    class Meta:
        verbose_name="Cast"
        verbose_name_plural = "Casts"

    def __str__(self) -> str:
        return self.name

class Crew(models.Model):
    '''
    Class crew for movies and tv shows.
    '''
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    known_for_department = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    adult = models.BooleanField(blank=True,null=True)
    gender = models.IntegerField()
    original_name = models.CharField(max_length=255)
    popularity = models.FloatField(blank=True)
    profile_path = models.TextField(blank=True, null=True)
    credit_id = models.CharField(max_length=255)

    class Meta:
        verbose_name="Crew"
        verbose_name_plural = "Crews"

    def __str__(self) -> str:
        return self.name

class Credit(models.Model):
    '''
    Class : Credits movies and tv shows.
    Description : This class is used to store the credits of a movie or tv show.
    '''
    id = models.IntegerField(primary_key=True)
    media_type = models.CharField(max_length=5,choices=MediaType.choices,default=MediaType.Movie)
    cast = models.ManyToManyField(Cast)
    crew = models.ManyToManyField(Crew)    

    class Meta:
        verbose_name="Credit"
        verbose_name_plural = "Credits"

    def __str__(self) -> str:
        return 'Credit : {}'.format(self.id)

class RequestApi(models.Model):
    '''
    This class is used to store the requests of the API.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    application_name = models.CharField(max_length=255)
    description = models.TextField()
    enable = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published',auto_now=True)

    class Meta:
        verbose_name="Request API"
        verbose_name_plural = "Requests API"

    def __str__(self) -> str:
        return 'Request API : {}'.format(self.application_name)