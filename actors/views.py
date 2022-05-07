from django.views.generic import TemplateView

from ESGI_Movies.wrappe.tmdb import tmdb_people

TEMPLATE_BASE = 'pages/actors/'

class BasePageView(TemplateView):
    template_name = TEMPLATE_BASE + 'actors.html'

# Class des acteurs
class PopularPageView(BasePageView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        actors = tmdb_people()
        context['actors'] = actors.popular(language='fr')['results']
        return context

# Class du détail d'un films
class ActorPageView(TemplateView):

    template_name = TEMPLATE_BASE + 'actor.html'

    def get_context_data(self, actor_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        actor = tmdb_people(actor_id)
        context['actor'] = actor.detail(language='fr')
        return context