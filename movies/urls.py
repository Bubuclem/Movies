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

    # URL Films détail
    path('movie/<int:movie_id>', 
    views.MovieDetailView.as_view(), 
    name='movie-detail'),

    # URL TV
    path('tv', 
    views.TVView.as_view(), 
    name='tv'),

    # URL Série détail
    path('tv/<int:tv_id>', 
    views.TVDetailView.as_view(), 
    name='tv-detail'),

    # URL Genres
    path('genres', 
    views.GenresView.as_view(), 
    name='genres'),

    # URL Poeples
    path('peoples', 
    views.PeoplesView.as_view(), 
    name='peoples'),

    # URL Peoples détail
    path('people/<int:people_id>', 
    views.PeoplesDetailView.as_view(), 
    name='people-detail'),

    # URL Videos
    path('videos', 
    views.VideosView.as_view(), 
    name='videos'),
    
    # URL Profile
    path('account', 
    views.AccountView.as_view(), 
    name='account'),

    # URL Utilisateurs
    path('users', 
    views.UsersView.as_view(), 
    name='users'),

    # URL Search
    path('search', 
    views.SearchView.as_view(), 
    name='search'),

    # URL Login
    path('login', 
    views.LoginView.as_view(), 
    name='login'),

    # URL logout
    path('logout', 
    views.LogoutView.as_view(), 
    name='logout')
]