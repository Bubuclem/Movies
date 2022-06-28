from datetime import datetime, timedelta

from rest_framework import viewsets
from rest_framework import permissions

from ESGI_Movies.wrappe.tmdb import tmdb_movie
from .serializers import MovieSerializer, ShowSerializer, ActorSerializer
from movies.models import Movie
from shows.models import Show
from actors.models import Actor

#
# Movies section
class MoviesPopularViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies popular to be viewed or edited.
    """
    queryset = Movie.objects.all().order_by('-popularity')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

class MoviesTopRatedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies top rated to be viewed or edited.
    """
    queryset = Movie.objects.all().filter(vote_count__gte=500).order_by('-vote_average', '-vote_count')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

class MoviesUpcomingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies upcoming to be viewed or edited.
    """
    queryset = Movie.objects.filter(status='Post Production').filter(release_date__gte=datetime.now() + timedelta(days=1))
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

class MoviesNowPlayingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies now playing to be viewed or edited.
    """
    queryset = Movie.objects.filter(status='Released').filter(release_date__gte=datetime.now() - timedelta(days=30))
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

class MoviesLastestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies lastest to be viewed or edited.
    """
    queryset = Movie.objects.all().filter(release_date__lte=datetime(datetime.now().year,datetime.now().month,1)).order_by('-release_date')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows by id movie to be viewed or edited.
    """
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Movie.objects.filter(id=self.kwargs['pk']).prefetch_related('genres', 'languages')

#
# Show section
class ShowsPopularViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows shows to be viewed or edited.
    '''
    queryset = Show.objects.all().order_by('-popularity')
    serializer_class = ShowSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShowsTopRatedViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows shows to be viewed or edited.
    Get shows order by vote average with 500 vote_count minimum
    '''
    queryset = Show.objects.all().order_by('-vote_average', '-vote_count').filter(vote_count__gte=500)
    serializer_class = ShowSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShowsOnTheAirViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows shows to be viewed or edited.
    Get shows order by release date with 500 vote_count minimum
    '''
    queryset = Show.objects.filter(status='Returning Series').filter(first_air_date__gte=datetime.now() - timedelta(days=30))
    serializer_class = ShowSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShowsLastestViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows shows to be viewed or edited.
    Get shows order by release date
    '''
    queryset = Show.objects.all().order_by('-first_air_date')
    serializer_class = ShowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Show.objects.filter(status='Returning Series').filter(first_air_date__gte=datetime.now() - timedelta(days=30))

class ShowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows by id show to be viewed or edited.
    """
    serializer_class = ShowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Show.objects.filter(id=self.kwargs['pk'])

class ActorsViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows actors to be viewed or edited.
    '''
    queryset = Actor.objects.all().order_by('-popularity')
    serializer_class = ActorSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActorViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows actors to be viewed
    '''
    serializer_class = ActorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Actor.objects.filter(id=self.kwargs['pk'])

class CreditsViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows actors to be viewed
    '''
    serializer_class = ActorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        movie_credits = tmdb_movie(self.kwargs['pk'])
        movie_credits = movie_credits.credits(language='fr')

        credits : Actor = sorted(movie_credits['cast'], key=lambda k: k['popularity'], reverse=True)

        return credits