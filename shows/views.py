from django.views.generic import TemplateView

from ESGI_Movies.wrappe.tmdb import tmdb_tv, tmdb_search
from .forms import SearchForm

TEMPLATE_BASE = 'pages/shows/'

class BasePageView(TemplateView):
    template_name = TEMPLATE_BASE + 'shows.html'

class PopularPageView(BasePageView):
    """
    Class des séries populaires.
    Retourne la liste des séries populaires.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        shows = tmdb_tv()
        context['shows'] = shows.popular(language='fr')['results']
        context['form'] = SearchForm()
        return context

class NowPlayingPageView(BasePageView):
    """
    Class des séries du moment.
    Retourne la liste des séries du moment.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        shows = tmdb_tv()
        context['shows'] = shows.on_the_air(language='fr')['results']
        return context

class SearchPageView(BasePageView):
    """
    Class recherche d'une série.
    Retourne la liste des séries de la recherche.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        shows = tmdb_search()
        context['shows'] = shows.show(query=self.request.GET.get("q"))['results']
        return context

class ShowPageView(TemplateView):
    """
    Class du détail d'une série.
    Retourne le détail, acteurs, vidéos et avis d'une série.
    """
    template_name = TEMPLATE_BASE + 'show.html'

    def get_context_data(self, show_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        show = tmdb_tv(show_id)
        context['show'] = show.detail(language='fr')
        context['credits'] = show.credits(language='fr')['cast'][:8]
        context['videos'] = show.videos(language='fr')['results'][:4]
        context['reviews'] = show.reviews(language='fr')['results'][:5]
        return context

class CreditsPageView(TemplateView):
    """
    Class des acteurs d'une série.
    Retourne le détail, acteurs d'une série.
    """
    template_name = TEMPLATE_BASE + 'credits/credits.html'

    def get_context_data(self, show_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        show = tmdb_tv(show_id)
        context['show'] = show.detail(language='fr')
        context['credits'] = show.credits(language='fr')['cast']
        
        return context

class VideosPageView(TemplateView):
    """
    Class des vidéos d'une série.
    Retourne le détail, vidéos d'une série.
    """
    template_name = TEMPLATE_BASE + 'videos/videos.html'

    def get_context_data(self, show_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        show = tmdb_tv(show_id)
        context['movie'] = show.detail(language='fr')
        context['videos'] = show.videos(language='fr')['results']
        
        return context

class ReviewsPageView(TemplateView):
    """
    Class des avis d'une série.
    Retourne le détail, avis d'une série.
    """
    template_name = TEMPLATE_BASE + 'reviews/reviews.html'

    def get_context_data(self, show_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        show = tmdb_tv(show_id)
        context['movie'] = show.detail(language='fr')
        context['reviews'] = show.reviews(language='fr')['results']
        
        return context