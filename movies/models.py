from statistics import mode
from django.db import models

class Utilisateur(models.Model):
    id      = models.IntegerField(primary_key=True)
    token   = models.UUIDField()
    email   = models.EmailField()

class Video(models.Model):
    id = models.IntegerField(primary_key=True)

class People(models.Model):
    id = models.IntegerField(primary_key=True)

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)

class Media(models.Model):
    id                  = models.IntegerField(primary_key=True)
    overview            = models.CharField(max_length=200)
    poster_path         = models.CharField(max_length=200)
    popularity          = models.FloatField(max_length=200)
    backdrop_path       = models.CharField(max_length=200)
    vote_average        = models.FloatField()
    release_date        = models.CharField(max_length=200)
    original_language   = models.CharField(max_length=200)
    genre_ids           = models.JSONField(max_length=200)
    vote_count          = models.IntegerField()
    title               = models.CharField(max_length=200)
    original_title      = models.CharField(max_length=200)
    origin_country      = models.JSONField()
    video               = models.BooleanField()
    adult               = models.BooleanField()

    budget              = models.IntegerField()
    revenue             = models.IntegerField()
    runtime             = models.IntegerField()
    status              = models.CharField(max_length=200)
    tagline             = models.CharField(max_length=200)