import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Watched(models.Model):
    
    class MediaType(models.TextChoices):
            Movie = 'movie',
            Show = 'tv',

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    media_id = models.IntegerField()
    media_type = models.CharField(max_length=5,choices=MediaType.choices,default=MediaType.Movie)
    pub_date = models.DateTimeField('date published',auto_now=True)
    def __str__(self) -> str:
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Review(models.Model):

    class MediaType(models.TextChoices):
        Movie = 'movie',
        Show = 'tv',

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    media_id = models.IntegerField()
    media_type = models.CharField(max_length=5,choices=MediaType.choices,default=MediaType.Movie)
    pub_date = models.DateTimeField('date published')
    def __str__(self) -> str:
        return self.content

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)