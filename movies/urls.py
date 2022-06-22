from django.urls import path

from .views import PopularPageView, NowPlayingPageView, UpcomingPageView, TopRatedPageView,MoviePageView, SearchPageView

app_name = 'movies'
urlpatterns = [
    # URL des films populaires
    path('populaires/', 
    PopularPageView.as_view(), 
    name='popular'),

    # URL des films du moment
    path('du-moment/', 
    NowPlayingPageView.as_view(), 
    name='nowplaying'),

    # URL des films à venir
    path('a-venir/', 
    UpcomingPageView.as_view(), 
    name='upcoming'),

    # URL des films les mieux notés
    path('les-mieux-notes/',
    TopRatedPageView.as_view(),
    name='toprated'),

    # URL de recherche de films
    path('recherche/',
    SearchPageView.as_view(),
    name='search'),

    # URL du détail d'un film
    path('<int:movie_id>/', 
    MoviePageView.as_view(), 
    name='detail'),
]