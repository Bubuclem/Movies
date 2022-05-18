from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import View

from ESGI_Movies.wrappe.tmdb import tmdb_people, tmdb_search
from .forms import SearchForm

TEMPLATE_BASE = 'pages/actors/'

class BasePageView(TemplateView):
    template_name = TEMPLATE_BASE + 'actors.html'

class PopularPageView(BasePageView):
    """
    Class des acteurs
    Retourne la liste des acteurs
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        actors = tmdb_people()
        context['actors'] = actors.popular(language='fr')['results']
        context['form'] = SearchForm()
        return context

class SearchPageView(BasePageView):
    """
    Class recherche d'un acteur.
    Retourne la liste des acteurs de la recherche.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        person = tmdb_search()
        context['actors'] = person.person(query=self.request.GET.get("q"))['results']
        return context

class ActorPageView(TemplateView):
    """
    Class du détail d'un acteur
    Retourn les détails d'un acteur
    """
    template_name = TEMPLATE_BASE + 'actor.html'

    def get_context_data(self, actor_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        actor = tmdb_people(actor_id)
        context['actor'] = actor.detail(language='fr')
        return context