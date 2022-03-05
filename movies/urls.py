from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    # URL Media - Page principal
    path('', 
    views.MediaView.as_view(), 
    name='media'),

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
    
    # URL Utilisateurs
    path('utilisateurs', 
    views.UtilisateursView.as_view(), 
    name='utilisateurs'),

    # URL Login
    path('login', 
    views.LoginView.as_view(), 
    name='login'),

    # URL logout
    path('logout', 
    views.LogoutView.as_view(), 
    name='logout')
]