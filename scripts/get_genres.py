from movies.models import Genre as MovieGenre
from shows.models import Genre as ShowGenre
from ESGI_Movies.wrappe.tmdb import tmdb_genres

def get_movies_genres():
    '''
    Get all movies genres from TMDB and save them in the database
    '''
    genres = tmdb_genres()
    genres = genres.movie_list(language='fr')
    for genre in genres['genres']:
        if MovieGenre.objects.filter(id=genre['id']).exists() is False:
            MovieGenre.objects.create(
                id=genre['id'],
                name=genre['name']
            )

def get_tv_shows_genres():
    '''
    Get all tv shows genres from TMDB and save them in the database
    '''
    genres = tmdb_genres()
    genres = genres.tv_list(language='fr')
    for genre in genres['genres']:
        if ShowGenre.objects.filter(id=genre['id']).exists() is False:
            ShowGenre.objects.create(
                id=genre['id'],
                name=genre['name']
            )

def run():
    get_movies_genres()
    get_tv_shows_genres()