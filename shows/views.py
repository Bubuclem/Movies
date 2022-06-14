from datetime import datetime, timedelta

from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView, ListView

from ESGI_Movies.wrappe.tmdb import tmdb_tv, tmdb_search, tmdb_genres
from .models import Show
from management.forms import ReviewForm
from management.models import Watched, Review

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

class SearchPageView(TemplateView):
    """
    Class recherche d'une série.
    Retourne la liste des séries de la recherche.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        shows = tmdb_search()
        context['shows'] = shows.show(language='fr',query=self.request.GET.get("q"))['results']
        return context

class ShowPageView(TemplateView):
    """
    Class du détail d'une série.
    Retourne le détail, acteurs, vidéos et avis d'une série.
    """
    template_name = TEMPLATE_BASE + 'show.html'

    def get_context_data(self, show_id,**kwargs):
        context = super().get_context_data(**kwargs)

        show = tmdb_tv(show_id)
        tmdb_data = show.detail(language='fr')

        try:
            show : Show = Show.objects.get(id=show_id)
            show.vote_average=tmdb_data['vote_average']
            show.vote_count=tmdb_data['vote_count']
            show.popularity=tmdb_data['popularity']
            show.save()
        except Show.DoesNotExist:
            show = Show.objects.create(
                id=tmdb_data['id'],
                name=tmdb_data['name'],
                overview=tmdb_data['overview'],
                first_air_date=tmdb_data['first_air_date'],
                last_air_date=tmdb_data['last_air_date'],
                poster_path=tmdb_data['poster_path'],
                vote_average=tmdb_data['vote_average'],
                vote_count=tmdb_data['vote_count'],
                popularity=tmdb_data['popularity'],
                adult=tmdb_data['adult'],
                original_language=tmdb_data['original_language'],
                original_title=tmdb_data['original_title']
            )

        context['show'] = show
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