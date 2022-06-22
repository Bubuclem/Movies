from django.urls import path

from .views import PopularPageView, NowPlayingPageView, LastestPageView,ShowPageView, SearchPageView, TopRatedPageView

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
    name='detail')
]