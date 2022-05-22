from django.urls import path

from .views import PopularPageView, NowPlayingPageView, UpcomingPageView, MoviePageView, CreditsPageView, VideosPageView, ReviewsPageView, SearchPageView, WriteReviewPageView

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

    # URL de recherche de films
    path('recherche/',
    SearchPageView.as_view(),
    name='search'),

    # URL du détail d'un film
    path('<int:movie_id>/', 
    MoviePageView.as_view(), 
    name='detail'),

    # URL des crédits d'un film
    path('<int:movie_id>/credits/', 
    CreditsPageView.as_view(), 
    name='credits'),

    # URL des vidéos d'un film
    path('<int:movie_id>/videos/', 
    VideosPageView.as_view(), 
    name='videos'),

    # URL des avis d'un film
    path('<int:movie_id>/avis/', 
    ReviewsPageView.as_view(), 
    name='reviews'),

    # URL pour rédiger un avis
    path('<int:movie_id>/avis/edition/', 
    WriteReviewPageView.as_view(), 
    name='writereview')
]