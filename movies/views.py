from django.views.generic import TemplateView

from ESGI_Movies.wrappe.tmdb import tmdb_movie, tmdb_search, tmdb_genres

TEMPLATE_BASE = 'pages/movies/'

class BasePageView(TemplateView):
    template_name = TEMPLATE_BASE + 'movies.html'

# Class des films populaires
class PopularPageView(BasePageView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movies = tmdb_movie()
        context['movies'] = movies.popular(language='fr')['results']
        return context

# Class des films du moment
class NowPlayingPageView(BasePageView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movies = tmdb_movie()
        context['movies'] = movies.now_playing(language='fr')['results']
        return context

# Class des films à venir
class UpcomingPageView(BasePageView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movies = tmdb_movie()
        context['movies'] = movies.upcoming(language='fr')['results']
        return context

# Class du détail d'un films
class MoviePageView(TemplateView):

    template_name = TEMPLATE_BASE + 'movie.html'

    def get_context_data(self, movie_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movie = tmdb_movie(movie_id)
        context['movie'] = movie.detail(language='fr')
        context['credits'] = movie.credits(language='fr')['cast'][:8]
        context['videos'] = movie.videos(language='fr')['results'][:4]
        context['reviews'] = movie.reviews(language='fr')['results'][:5]

        return context

# Class des crédits d'un films
class CreditsPageView(TemplateView):

    template_name = TEMPLATE_BASE + 'credits/credits.html'

    def get_context_data(self, movie_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movie = tmdb_movie(movie_id)
        context['movie'] = movie.detail(language='fr')
        context['credits'] = movie.credits(language='fr')['cast']
        
        return context

# Class des vidéos d'un films
class VideosPageView(TemplateView):

    template_name = TEMPLATE_BASE + 'videos/videos.html'

    def get_context_data(self, movie_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movie = tmdb_movie(movie_id)
        context['movie'] = movie.detail(language='fr')
        context['videos'] = movie.videos(language='fr')['results']
        
        return context

# Class des avis d'un films
class ReviewsPageView(TemplateView):

    template_name = TEMPLATE_BASE + 'reviews/reviews.html'

    def get_context_data(self, movie_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movie = tmdb_movie(movie_id)
        context['movie'] = movie.detail(language='fr')
        context['reviews'] = movie.reviews(language='fr')['results']
        
        return context