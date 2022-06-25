from django.urls import path
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from management.views import LoginPageView, LogoutPageView, PasswordPageView, UserManagementPageView, UserManagementDetailPageView, ActiveUserPageView
from management.views import RegisterAccountPageView, AccountPageView, RequestApiPageView
from management.views import MoviesPageView, MoviePageView, ShowsPageView, ShowPageView
from management.views import WatchlistPageView, FavoritesPageView, ReviewsPageView, ReviewsDetailPageView

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

    # URL sécurité
    path('dashboard/securite/',
    login_required(PasswordPageView.as_view()),
    name='password'),

    # URL demande d'API
    path('dashboard/demande-api/',
    login_required(RequestApiPageView.as_view()),
    name='request-api'),

    # URL pour modifier un avis
    path('dashboard/avis/<int:pk>/',
    login_required(ReviewsDetailPageView.as_view()),
    name='reviews_detail'),

    path('dashboard/utilisateurs/',
    login_required(UserManagementPageView.as_view()),
    name='users'),

    path('dashboard/utilisateur/active/<int:pk>/',
    login_required(ActiveUserPageView.as_view()),
    name='active_user'),

    path('dashboard/utilisateur/<str:pk>/',
    login_required(UserManagementDetailPageView.as_view()),
    name='user_detail'),
]