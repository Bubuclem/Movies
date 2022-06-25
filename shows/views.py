from datetime import datetime, timedelta

from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView, ListView

from ESGI_Movies.wrappe.tmdb import tmdb_tv, tmdb_search
from .models import Show
from management.forms import ReviewForm
from management.models import Watched, Favorite, Review

TEMPLATE_BASE = 'pages/shows/'

class PopularPageView(ListView):
    """
    Class des séries populaires.
    Retourne la liste des séries populaires.
    """
    model = Show
    paginate_by = 20
    context_object_name = 'shows'
    ordering = ['-popularity']
    template_name = TEMPLATE_BASE + 'shows.html'

class NowPlayingPageView(ListView):
    """
    Class des séries du moment.
    Retourne la liste des séries du moment.
    """
    model = Show
    paginate_by = 20
    context_object_name = 'shows'
    template_name = TEMPLATE_BASE + 'shows.html'

    '''
    Check if release date is curent month
    '''
    def get_queryset(self):
        return Show.objects.filter(status='Returning Series').filter(first_air_date__gte=datetime.now() - timedelta(days=30))

class TopRatedPageView(ListView):
    '''
    Top rated shows class
    Return the top rated shows order by vote average with 500 vote_count minimum
    '''
    model = Show
    paginate_by = 20
    context_object_name = 'shows'
    ordering = ['-vote_average']
    template_name = TEMPLATE_BASE + 'shows.html'

    def get_queryset(self):
        return Show.objects.all().filter(vote_count__gte=500).order_by('-vote_average', '-vote_count')

class LastestPageView(ListView):
    """
    Class des séries les plus récentes.
    Retourne la liste des séries les plus récentes.
    """
    model = Show
    paginate_by = 20
    context_object_name = 'shows'
    ordering = ['-first_air_date']
    template_name = TEMPLATE_BASE + 'shows.html'

    def get_queryset(self):
        return Show.objects.filter(status='Returning Series').filter(first_air_date__gte=datetime.now() - timedelta(days=30))

class SearchPageView(ListView):
    """
    Class recherche d'une série.
    Retourne la liste des séries de la recherche.
    """
    model = Show
    paginate_by = 20
    context_object_name = 'shows'
    template_name = TEMPLATE_BASE + 'shows.html'

    def get_queryset(self):
        shows = tmdb_search().show(language='fr',query=self.request.GET.get("q"))['results']

        shows_ids = []
        for show in shows:
            shows_ids.append(show['id'])

            if Show.objects.filter(id=show['id']).exists() is False:
                Show.objects.create(
                    id=show['id'],
                    name=show['name'],
                    overview=show['overview'],
                    poster_path=show['poster_path'],
                    vote_average=show['vote_average'],
                    vote_count=show['vote_count'],
                    popularity=show['popularity'],
                    original_language=show['original_language']
                )

        return Show.objects.filter(id__in=shows_ids).order_by('-popularity')

class ShowPageView(TemplateView):
    """
    Class du détail d'une série.
    Retourne le détail, acteurs, vidéos et avis d'une série.
    """
    template_name = TEMPLATE_BASE + 'show.html'

    def get_context_data(self, show_id,**kwargs):
        context = super().get_context_data(**kwargs)

        show = tmdb_tv(show_id).detail(language='fr')

        try:
            _show : Show = Show.objects.get(id=show_id)
            _show.vote_average=show['vote_average']
            _show.vote_count=show['vote_count']
            _show.popularity=show['popularity']
            _show.save()
        except Show.DoesNotExist:
            _show = Show.objects.create(
                id=show['id'],
                name=show['name'],
                overview=show['overview'],
                first_air_date=show['first_air_date'],
                last_air_date=show['last_air_date'],
                poster_path=show['poster_path'],
                vote_average=show['vote_average'],
                vote_count=show['vote_count'],
                popularity=show['popularity'],
                original_language=show['original_language'],
                original_name=show['original_name']
            )

        context['show'] = _show

        show_cast = tmdb_tv(show_id).credits(language='fr')['cast']
        # Sort by popularity
        context['cast'] = sorted(show_cast, key=lambda k: k['popularity'], reverse=True)

        show_reviews = tmdb_tv(show_id).reviews(language='fr')['results']
        # Sort by date created
        context['reviews'] = sorted(show_reviews, key=lambda k: k['created_at'], reverse=True)[:5]
        if Review.objects.filter(media_id=_show.id).exists():
            context['reviews'].append(Review.objects.get(media_id=_show.id,media_type='show'))

        # Sort by vote average
        context['similars'] = tmdb_tv(show_id).recommendations(language='fr')['results'][:8]

        if self.request.user.is_authenticated:
            try :
                context['watched'] = Watched.objects.get(user=self.request.user, media_id=show_id,media_type='show')
            except Watched.DoesNotExist:
                context['watched'] = None

            try :
                context['favorite'] = Favorite.objects.get(user=self.request.user, media_id=show_id,media_type='show')
            except Favorite.DoesNotExist:
                context['favorite'] = None

            context['form_review'] = ReviewForm()

        return context

    def post(self, request, show_id, **kwargs):
        show = Show.objects.get(id=show_id)

        if 'watched' in request.POST:
            try :
                watched_movie = Watched.objects.get(user=request.user, media_id=show_id,media_type='show')
                watched_movie.delete()
            except Watched.DoesNotExist:
                Watched.objects.create(user=request.user, name=show.name, media_id=show_id, media_type='show')

        if 'favorite' in request.POST:
            try :
                favorite_movie = Favorite.objects.get(user=request.user, media_id=show_id,media_type='show')
                favorite_movie.delete()
            except Favorite.DoesNotExist:
                Favorite.objects.create(user=request.user, name=show.name, media_id=show_id, media_type='show')

        form_review = ReviewForm(request.POST)
        if form_review.is_valid():
            Review.objects.create(
                user=request.user,
                media_id=show_id,
                name=show.name,
                media_type='show',
                content=form_review.cleaned_data['content']
            )

        return redirect('/series/{}'.format(show_id))

class EpisodesPageView(TemplateView):
    """
    Class des épisodes d'une série.
    Retourne la liste des épisodes d'une série.
    """
    template_name = TEMPLATE_BASE + 'episodes.html'

    def get_context_data(self, show_id, season_number,**kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = Show.objects.get(id=show_id)
        context['episodes'] = tmdb_tv(show_id).season(season_number=season_number, language='fr')['episodes']

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
    template_name = 'generic/reviews/reviews.html'

    def get_context_data(self, show_id, **kwargs):
        context = super().get_context_data(**kwargs)
        
        show = tmdb_tv(show_id)
        context['movie'] = show.detail(language='fr')
        context['reviews'] = show.reviews(language='fr')['results']
        
        return context

class WriteReviewPageView(View):
    '''
    Class pour rédiger un avis sur un film.
    get() :
    Retourne le formulaire pour rédiger un avis.
    post() :
    Enregistre le formulaire si il est valide.
    '''
    def get(self,request,show_id):
        if self.request.user.is_authenticated:
            form = ReviewForm()

            show = tmdb_tv(show_id)
            show_detail = show.detail(language='fr')

            return render(request,'generic/reviews/write.html',{'form': form, 'show': show_detail})
        return redirect('/authentification/')

    def post(self,request,show_id):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review()
            review.user = self.request.user
            review.content = form.cleaned_data['content']
            review.media_id = show_id
            review.media_type = Review.MediaType.Show

            review.save()

        return redirect(ReviewsPageView.as_view)