from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from ESGI_Movies.wrappe.tmdb import tmdb_movie, tmdb_search, tmdb_genres
from management.forms import ReviewForm
from management.models import Watched

TEMPLATE_BASE = 'pages/movies/'

class PopularPageView(TemplateView, View):
    """
    Class des films populaires.
    Retourne la liste des films populaires en francais.
    """
    template_name = TEMPLATE_BASE + 'movies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movies = tmdb_movie()
        context['movies'] = movies.popular(language='fr')['results']
        
        genres = tmdb_genres()
        context['genres'] = genres.movie_list(language='fr')['genres']

        return context
    
    def post(self,**kwargs):
        print('Post')

class NowPlayingPageView(TemplateView):
    """
    Class des films du moment.
    Retourne la liste des films du moment en francais.
    """
    template_name = TEMPLATE_BASE + 'movies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movies = tmdb_movie()
        context['movies'] = movies.now_playing(language='fr')['results']

        genres = tmdb_genres()
        context['genres'] = genres.movie_list(language='fr')['genres']

        return context

class UpcomingPageView(TemplateView):
    """
    Class des films à venir.
    Retourne la liste des films à venir en francais.
    """
    template_name = TEMPLATE_BASE + 'movies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movies = tmdb_movie()
        context['movies'] = movies.upcoming(language='fr')['results']

        genres = tmdb_genres()
        context['genres'] = genres.movie_list(language='fr')['genres']

        return context

class SearchPageView(TemplateView):
    """
    Class recherche d'un film.
    Retourne la liste des films de la recherche.
    """
    template_name = TEMPLATE_BASE + 'movies.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movie = tmdb_search()
        context['movies'] = movie.movie(language='fr',query=self.request.GET.get("q"))['results']
        return context

class MoviePageView(View):
    """
    Class du détail d'un film.
    Retourne les détails, 8 acteurs, 4 vidéos, 5 avis du film.
    """
    template_name = TEMPLATE_BASE + 'movie.html'

    def get(self, request, movie_id):
        context =  self._get(request, movie_id)
        
        try:
            watch = Watched.objects.get(media_id=movie_id,media_type=Watched.MediaType.Movie)
        except:
            watch = None

        context['watch'] = watch

        return render(request,TEMPLATE_BASE + 'movie.html',context)

    def post(self, request, movie_id):
        context =  self._get(request, movie_id)

        try:
            watch = Watched.objects.get(media_id=movie_id,media_type=Watched.MediaType.Movie)
            watch.delete()
            watch = None
        except:
            watch = Watched()
            watch.user = self.request.user
            watch.name = context.get('movie').get('title')
            watch.media_id = movie_id
            watch.media_type = Watched.MediaType.Movie
            watch.save()

        context['watch'] = watch

        return render(request,TEMPLATE_BASE + 'movie.html',context)

    def _get(self, request, movie_id):
        data = tmdb_movie(movie_id)
        movie = data.detail(language='fr')
        credits = data.credits(language='fr')['cast'][:8]
        videos = data.videos(language='fr')['results'][:4]
        reviews = data.reviews(language='fr')['results'][:5]
        
        context = {'movie': movie,'credits': credits,'videos': videos,'reviews': reviews}

        return context

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