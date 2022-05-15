from django.views.generic import TemplateView

from ESGI_Movies.wrappe.tmdb import tmdb_tv

TEMPLATE_BASE = 'pages/shows/'

class BasePageView(TemplateView):
    template_name = TEMPLATE_BASE + 'shows.html'

# Class des séries populaires
class PopularPageView(BasePageView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        shows = tmdb_tv()
        context['shows'] = shows.popular(language='fr')['results']
        return context

# Class des séries du moment
class NowPlayingPageView(BasePageView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        shows = tmdb_tv()
        context['shows'] = shows.on_the_air(language='fr')['results']
        return context

# Class du détail d'une série
class ShowPageView(TemplateView):

    template_name = TEMPLATE_BASE + 'show.html'

    def get_context_data(self, show_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        show = tmdb_tv(show_id)
        context['show'] = show.detail(language='fr')
        context['credits'] = show.credits(language='fr')['cast'][:8]
        context['videos'] = show.videos(language='fr')['results'][:4]
        context['reviews'] = show.reviews(language='fr')['results'][:5]
        return context

# Class des crédits d'une série
class CreditsPageView(TemplateView):

    template_name = TEMPLATE_BASE + 'credits/credits.html'

    def get_context_data(self, show_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        show = tmdb_tv(show_id)
        context['show'] = show.detail(language='fr')
        context['movie'] = show.detail(language='fr')
        context['credits'] = show.credits(language='fr')['cast']
        
        return context

# Class des vidéos d'une série
class VideosPageView(TemplateView):

    template_name = TEMPLATE_BASE + 'videos/videos.html'

    def get_context_data(self, show_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        show = tmdb_tv(show_id)
        context['movie'] = show.detail(language='fr')
        context['videos'] = show.videos(language='fr')['results']
        
        return context

# Class des avis d'une série
class ReviewsPageView(TemplateView):

    template_name = TEMPLATE_BASE + 'reviews/reviews.html'

    def get_context_data(self, show_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        show = tmdb_tv(show_id)
        context['movie'] = show.detail(language='fr')
        context['reviews'] = show.reviews(language='fr')['results']
        
        return context