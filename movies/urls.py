from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    # URL Films - Page principal
    path('', 
    views.MoviesView.as_view(), 
    name='movies'),
    
    # Films
    # =====
    # URL Films - Populaire
    path('films', 
    views.MoviesView.as_view(), 
    name='movies'),

    # URL Films - Type
    path('films/<str:type>', 
    views.MoviesView.as_view(), 
    name='movies'),

    # URL Films - Populaire - Page
    path('films/<int:page>', 
    views.MoviesView.as_view(), 
    name='movies'),

    # URL Films - Type - Page
    path('films/<int:page>/<str:type>', 
    views.MoviesView.as_view(), 
    name='movies'),

    # URL Films - Détails
    path('film/<int:movie_id>', 
    views.MovieDetailView.as_view(), 
    name='movie-detail'),
    
    # URL Profile
    path('account', 
    views.AccountView.as_view(), 
    name='account'),

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