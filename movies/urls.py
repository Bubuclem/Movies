from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    # URL Media - Page principal
    path('', 
    views.MediaView.as_view(), 
    name='media'),

    # URL Films
    path('movies', 
    views.MoviesView.as_view(), 
    name='movies'),

    # URL TV
    path('tv', 
    views.TVView.as_view(), 
    name='tv'),

    # URL Genres
    path('genres', 
    views.GenresView.as_view(), 
    name='genres'),

    # URL Poeples
    path('poeples', 
    views.PoeplesView.as_view(), 
    name='poeples'),

    # URL Videos
    path('videos', 
    views.VideosView.as_view(), 
    name='videos'),
    
    # URL Profile
    path('account', 
    views.AccountView.as_view(), 
    name='account'),

    # URL Utilisateurs
    path('Users', 
    views.UsersView.as_view(), 
    name='Users'),

    # URL Login
    path('login', 
    views.LoginView.as_view(), 
    name='login'),

    # URL logout
    path('logout', 
    views.LogoutView.as_view(), 
    name='logout')
]