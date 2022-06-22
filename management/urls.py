from django.urls import path
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from management.views import LoginPageView, LogoutPageView, RegisterAccountPageView,AccountPageView, MoviesPageView, MoviePageView, ShowsPageView, ShowPageView, WatchlistPageView, FavoritesPageView, ReviewsPageView, ReviewsDetailPageView, PasswordPageView, UserManagementPageView

app_name = 'management'
urlpatterns = [
    # URL / redirects to popular movies
    path('', 
    lambda req: redirect('/films/populaires/')),

    # URL de connexion
    path('authentification/', 
    LoginPageView.as_view(), 
    name='login'),

    # URL de déconnexion
    path('deconnexion/', 
    LogoutPageView.as_view(), 
    name='logout'),
    
    # URL de création de compte
    path('nouveau-compte/', 
    RegisterAccountPageView.as_view(), 
    name='register'),

    # URL du profile utilisateur
    path('dashboard/profile/', 
    login_required(AccountPageView.as_view()), 
    name='account'),

    # URL de la watchlist
    path('dashboard/watchlist/',
    login_required(WatchlistPageView.as_view()),
    name='watchlist'),

    # URL des favoris
    path('dashboard/favoris/',
    login_required(FavoritesPageView.as_view()),
    name='favoris'),

    # URL des avis
    path('dashboard/commentaires/',
    login_required(ReviewsPageView.as_view()),
    name='reviews'),

    # URL pour modifier un avis
    path('dashboard/avis/<int:pk>/',
    login_required(ReviewsDetailPageView.as_view()),
    name='reviews_detail'),

    path('dashboard/films/',
    MoviesPageView.as_view(),
    name='movies'),

    path('dashboard/film/<int:pk>/',
    MoviePageView.as_view(),
    name='movie'),

    path('dashboard/shows/',
    ShowsPageView.as_view(),
    name='shows'),

    path('dashboard/show/<int:pk>/',
    ShowPageView.as_view(),
    name='show'),

    path('dashboard/profile/password/',
    PasswordPageView.as_view(),
    name='password'),

    path('dashboard/utilisateurs/',
    UserManagementPageView.as_view(),
    name='users'),
]