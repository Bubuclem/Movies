from django.views.generic import TemplateView, ListView

from ESGI_Movies.wrappe.tmdb import tmdb_people, tmdb_search
from .models import Actor

TEMPLATE_BASE = 'pages/actors/'

class PopularPageView(ListView):
    """
    Class des acteurs
    Retourne la liste des acteurs
    """
    model = Actor
    paginate_by = 20
    context_object_name = 'actors'
    ordering = ['-popularity']
    template_name = TEMPLATE_BASE + 'actors.html'

class SearchPageView(ListView):
    """
    Class recherche d'un acteur.
    Retourne la liste des acteurs de la recherche.
    """
    model = Actor
    paginate_by = 20
    context_object_name = 'actors'
    template_name = TEMPLATE_BASE + 'actors.html'

    def get_queryset(self):
        persons = tmdb_search().person(language='fr',query=self.request.GET.get("q"))['results']

        persons_ids = []
        for person in persons:
            persons_ids.append(person['id'])

            if Actor.objects.filter(id=person['id']).exists() is False:
                Actor.objects.create(
                    id=person['id'],
                    name=person['name'],
                    profile_path=person['profile_path'],
                    popularity=person['popularity'],
                    adult=person['adult']
                )

        return Actor.objects.filter(id__in=persons_ids).order_by('-popularity')

class ActorPageView(TemplateView):
    """
    Actor View
    Get actor by id, get or update actor in database
    """
    template_name = TEMPLATE_BASE + 'actor.html'

    def get_context_data(self, actor_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        people = tmdb_people(actor_id)
        tmdb_actor = people.detail(language='fr')

        try:
            actor : Actor = Actor.objects.get(id=actor_id)
            actor.name = tmdb_actor['name']
            actor.popularity = tmdb_actor['popularity']
            actor.profile_path = tmdb_actor['profile_path']
            actor.known_for_department = tmdb_actor['known_for_department']
            actor.adult = tmdb_actor['adult']
            actor.birthday = tmdb_actor['birthday']
            actor.biography = tmdb_actor['biography']
            actor.deathday = tmdb_actor['deathday']
            actor.homepage = tmdb_actor['homepage']
            actor.gender = tmdb_actor['gender']
            actor.imdb_id = tmdb_actor['imdb_id']
            actor.save()
        except Actor.DoesNotExist:
            actor = Actor.objects.create(
                id=actor_id,
                name=tmdb_actor['name'],
                profile_path=tmdb_actor['profile_path'],
                popularity=tmdb_actor['popularity'],
                known_for_department=tmdb_actor['known_for_department'],
                adult=tmdb_actor['adult'],
                birthday=tmdb_actor['birthday'],
                biography=tmdb_actor['biography'],
                deathday=tmdb_actor['deathday'],
                homepage=tmdb_actor['homepage'],
                gender=tmdb_actor['gender'],
                imdb_id=tmdb_actor['imdb_id']
            )
        context['actor'] = actor

        return context