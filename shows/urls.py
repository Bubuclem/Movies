from django.urls import path

from .views import PopularPageView, NowPlayingPageView, LastestPageView,ShowPageView, CreditsPageView, VideosPageView, ReviewsPageView, SearchPageView, WriteReviewPageView, TopRatedPageView

app_name = 'shows'
urlpatterns = [    
    # URL des séries populaires
    path('populaires/', 
    PopularPageView.as_view(), 
    name='popular'),
    
    # URL des séries du moment
    path('du-moment/', 
    NowPlayingPageView.as_view(), 
    name='nowplaying'),

    # URL des séries les mieux notées
    path('les-mieux-notees/',
    TopRatedPageView.as_view(),
    name='toprated'),

    # URL des séries à venir
    path('a-venir/',
    LastestPageView.as_view(),
    name='upcoming'),

    # URL de recherche de séries
    path('recherche/',
    SearchPageView.as_view(),
    name='search'),

    # URL du détail d'une série
    path('<int:show_id>/', 
    ShowPageView.as_view(), 
    name='detail'),

    # URL des crédits d'un film
    path('<int:show_id>/credits/', 
    CreditsPageView.as_view(), 
    name='credits'),

    # URL des vidéos d'un film
    path('<int:show_id>/videos/', 
    VideosPageView.as_view(), 
    name='videos'),

    # URL des avis d'un film
    path('<int:show_id>/avis/', 
    ReviewsPageView.as_view(), 
    name='reviews'),

    # URL pour rédiger un avis
    path('<int:show_id>/avis/edition/', 
    WriteReviewPageView.as_view(), 
    name='writereview')
]