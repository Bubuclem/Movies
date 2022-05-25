from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from ESGI_Movies.wrappe.tmdb import tmdb_tv, tmdb_search, tmdb_genres
from management.forms import ReviewForm
from management.models import Watched, Review

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

        genres = tmdb_genres()
        context['genres'] = genres.movie_list(language='fr')['genres']

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

        genres = tmdb_genres()
        context['genres'] = genres.movie_list(language='fr')['genres']

        return context

class SearchPageView(BasePageView):
    """
    Class recherche d'une série.
    Retourne la liste des séries de la recherche.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        shows = tmdb_search()
        context['shows'] = shows.show(language='fr',query=self.request.GET.get("q"))['results']
        return context

class ShowPageView(View):
    """
    Class du détail d'une série.
    Retourne le détail, acteurs, vidéos et avis d'une série.
    """
    template_name = TEMPLATE_BASE + 'show.html'

    def get(self, request, show_id):
        context = self._get(show_id)

        try:
            watch = Watched.objects.get(media_id=show_id,media_type=Watched.MediaType.Show)
        except:
            watch = None

        context['watch'] = watch

        return render(request,TEMPLATE_BASE + 'show.html',context)

    def post(self, request, show_id):
        context =  self._get(show_id)

        try:
            watch = Watched.objects.get(media_id=show_id,media_type=Watched.MediaType.Show)
            watch.delete()
            watch = None
        except:
            watch = Watched()
            watch.user = self.request.user
            watch.name = context.get('show').get('name')
            watch.media_id = show_id
            watch.media_type = Watched.MediaType.Show
            watch.save()

        context['watch'] = watch

        return render(request,TEMPLATE_BASE + 'show.html',context)

    def _get(self, show_id):
        data = tmdb_tv(show_id)
        show = data.detail(language='fr')
        credits = data.credits(language='fr')['cast'][:8]
        videos = data.videos(language='fr')['results'][:4]
        reviews = data.reviews(language='fr')['results'][:5]
        
        context = {'show': show,'credits': credits,'videos': videos,'reviews': reviews}

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