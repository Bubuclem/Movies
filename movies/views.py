from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from ESGI_Movies.wrappe.tmdb import tmdb_movie, tmdb_search
from management.forms import ReviewForm
from management.models import Watched, Favorite, Review
from .models import Movie

TEMPLATE_BASE = 'pages/movies/'
 
class PopularPageView(ListView):
    """
    Class des films populaires.
    Retourne la liste des films populaires en francais.
    """
    model = Movie
    paginate_by = 20
    context_object_name = 'movies'
    ordering = ['-popularity']
    template_name = TEMPLATE_BASE + 'movies.html'

class NowPlayingPageView(ListView):
    """Class des films du moment.
    Retourne la liste des films du moment en francais.
    """
    model = Movie
    paginate_by = 20
    context_object_name = 'movies'
    template_name = TEMPLATE_BASE + 'movies.html'

    def get_queryset(self):
        '''Check if release date is among the current month
        '''
        return Movie.objects.filter(status='Released').filter(release_date__gte=datetime.now() - timedelta(days=30))

class UpcomingPageView(ListView):
    """Class des films à venir.
    Retourne la liste des films à venir en francais.
    """
    model = Movie
    paginate_by = 20
    context_object_name = 'movies'
    template_name = TEMPLATE_BASE + 'movies.html'

    def get_queryset(self):
        '''Check if release date is among the next days
        '''
        return Movie.objects.filter(status='Post Production').filter(release_date__gte=datetime.now() + timedelta(days=1))

class TopRatedPageView(ListView):
    """Class des films les mieux notés.
    Retourne la liste des films les mieux notés en francais.
    """
    model = Movie
    paginate_by = 20
    context_object_name = 'movies'
    ordering = ['-vote_average']
    template_name = TEMPLATE_BASE + 'movies.html'

    def get_queryset(self):
        return Movie.objects.filter(vote_count__gte=500).order_by('-vote_average', '-vote_count')

class SearchPageView(ListView):
    """Class recherche d'un film.
    Retourne la liste des films de la recherche.
    """
    model = Movie
    paginate_by = 20
    context_object_name = 'movies'
    template_name = TEMPLATE_BASE + 'movies.html'

    def get_queryset(self):        
        movies = tmdb_search().movie(language='fr',query=self.request.GET.get("q"))['results']

        movies_ids = []
        for movie in movies:
            movies_ids.append(movie['id'])

            if Movie.objects.filter(id=movie['id']).exists() is False:
                Movie.objects.create(
                    id=movie['id'],
                    title=movie['title'],
                    overview=movie['overview'],
                    poster_path=movie['poster_path'],
                    vote_average=movie['vote_average'],
                    vote_count=movie['vote_count'],
                    popularity=movie['popularity'],
                    adult=movie['adult'],
                    original_language=movie['original_language'],
                    original_title=movie['original_title']
                )

        return Movie.objects.filter(id__in=movies_ids).order_by('-popularity')

class MoviePageView(TemplateView):
    """Movie view.
    Get movie by id, get or update movie in database
    """
    template_name = TEMPLATE_BASE + 'movie.html'

    def get_context_data(self, movie_id,**kwargs):
        context = super().get_context_data(**kwargs)

        movie = tmdb_movie(movie_id)
        tmdb_data = movie.detail(language='fr')

        try:
            movie : Movie = Movie.objects.get(id=movie_id)
            movie.vote_average=tmdb_data['vote_average']
            movie.vote_count=tmdb_data['vote_count']
            movie.popularity=tmdb_data['popularity']
            movie.save()
        except Movie.DoesNotExist:
            movie = Movie.objects.create(
                id=tmdb_data['id'],
                title=tmdb_data['title'],
                overview=tmdb_data['overview'],
                release_date=tmdb_data['release_date'],
                poster_path=tmdb_data['poster_path'],
                vote_average=tmdb_data['vote_average'],
                vote_count=tmdb_data['vote_count'],
                popularity=tmdb_data['popularity'],
                adult=tmdb_data['adult'],
                original_language=tmdb_data['original_language'],
                original_title=tmdb_data['original_title']
            )

        context['movie'] = movie

        movie_credits = tmdb_movie(movie_id)
        movie_credits = movie_credits.credits(language='fr')
        # Sort by popularity
        context['cast'] = sorted(movie_credits['cast'], key=lambda k: k['popularity'], reverse=True)

        movie_reviews = tmdb_movie(movie_id)
        movie_reviews = movie_reviews.reviews(language='fr')
        # Sort by date created
        context['reviews'] = sorted(movie_reviews['results'], key=lambda k: k['created_at'], reverse=True)[:5]
        if Review.objects.filter(media_id=movie.id).exists():
            context['reviews'].append(Review.objects.get(media_id=movie.id,media_type='movie'))

        movies_similar = tmdb_movie(movie_id)
        movies_similar = movies_similar.recommendations(language='fr')
        # Sort by vote average
        context['similars'] = movies_similar['results'][:8]
        
        if self.request.user.is_authenticated:
            try :
                context['watched'] = Watched.objects.get(user=self.request.user, media_id=movie.id,media_type='movie')
            except Watched.DoesNotExist:
                context['watched'] = None
                
            try :
                context['favorite'] = Favorite.objects.get(user=self.request.user, media_id=movie.id,media_type='movie')
            except Favorite.DoesNotExist:
                context['favorite'] = None

            context['form_review'] = ReviewForm()

        return context

    def post(self, request, movie_id, **kwargs):
        movie = Movie.objects.get(id=movie_id)

        if 'watched' in request.POST:
            try :
                watched_movie = Watched.objects.get(user=request.user, media_id=movie.id,media_type='movie')
                watched_movie.delete()
            except Watched.DoesNotExist:
                Watched.objects.create(user=request.user, name=movie.title, media_id=movie.id, media_type='movie')

        if 'favorite' in request.POST:
            try :
                favorite_movie = Favorite.objects.get(user=request.user, media_id=movie.id,media_type='movie')
                favorite_movie.delete()
            except Favorite.DoesNotExist:
                Favorite.objects.create(user=request.user, name=movie.title, media_id=movie.id, media_type='movie')

        form_review = ReviewForm(request.POST)
        if form_review.is_valid():
            Review.objects.create(
                user=request.user,
                media_id=movie_id,
                name=movie.title,
                media_type='movie',
                content=form_review.cleaned_data['content']
            )

        return redirect('/films/{}'.format(movie_id))

class CreditsPageView(TemplateView):
    """
    Class des crédits d'un film.
    Retourne les détails, acteurs du film.
    """
    template_name = TEMPLATE_BASE + 'credits/credits.html'

    def get_context_data(self, movie_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movie = tmdb_movie(movie_id)
        context['movie'] = movie.detail(language='fr')
        context['credits'] = movie.credits(language='fr')['cast']
        
        return context

class VideosPageView(TemplateView):
    """
    Class des vidéos d'un film.
    Retourne les détails, vidéos du film.
    """
    template_name = TEMPLATE_BASE + 'videos/videos.html'

    def get_context_data(self, movie_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movie = tmdb_movie(movie_id)
        context['movie'] = movie.detail(language='fr')
        context['videos'] = movie.videos(language='fr')['results']
        
        return context

class ReviewsPageView(TemplateView):
    """
    Class des avis d'un film.
    Retourne les détails, avis du film.
    """
    template_name = 'generic/reviews/reviews.html'

    def get_context_data(self, movie_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movie = tmdb_movie(movie_id)
        context['movie'] = movie.detail(language='fr')
        context['reviews'] = movie.reviews(language='fr')['results']
        
        return context

class WriteReviewPageView(View):
    '''
    Class pour rédiger un avis sur un film.
    get() :
    Retourne le formulaire pour rédiger un avis.
    post() :
    Enregistre le formulaire si il est valide.
    '''
    def get(self,request,movie_id):
        form = ReviewForm()

        movie = tmdb_movie(movie_id)
        movie_detail = movie.detail(language='fr')

        return render(request,'generic/reviews/write.html',{'form': form, 'movie': movie_detail})

    def post():
        pass