from django.db import models

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=50)
    overview = models.TextField()
    release_date = models.DateField()
    original_title = models.CharField(max_length=50)
    original_language = models.CharField(max_length=2)
    backdrop_path = models.CharField(max_length=50)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()