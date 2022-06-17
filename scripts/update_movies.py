from movies.models import Movie
from ESGI_Movies.wrappe.tmdb import tmdb_movie

def update_top_rated_movies():
    ''' 
    Get the first five pages top rated movies from TMDB and save them in the database
    If a movie already exists in the database, update it
    '''
    for i in range(1,6):
        movies = tmdb_movie()
        movies = movies.top_rated(language='fr', page=i)
        for movie in movies['results']:
            json = get_detail_from_id(movie['id'])

            if Movie.objects.filter(id=movie['id']).exists():
                movie_update : Movie = Movie.objects.get(id=movie['id'])
                movie_update.convert_json_to_object(json)
                movie_update.save()
            else:
                movie_update : Movie = Movie()
                movie_update.convert_json_to_object(json)
                movie_update.save()

def update_popular_movies():
    '''
    Get the first five pages popular movies from TMDB and save them in the database
    If a movie already exists in the database, update it
    '''
    for i in range(1,6):
        movies = tmdb_movie()
        movies = movies.popular(language='fr', page=i)
        for movie in movies['results']:
            json = get_detail_from_id(movie['id'])

            if Movie.objects.filter(id=movie['id']).exists():
                movie_update : Movie = Movie.objects.get(id=movie['id'])
                movie_update.convert_json_to_object(json)
                movie_update.save()
            else:
                movie_update : Movie = Movie()
                movie_update.convert_json_to_object(json)
                movie_update.save()

def update_upcoming_movies():
    '''
    Get the first five pages upcoming movies from TMDB and save them in the database
    If a movie already exists in the database, update it
    '''
    for i in range(1,6):
        movies = tmdb_movie()
        movies = movies.upcoming(language='fr', page=i)
        for movie in movies['results']:
            json = get_detail_from_id(movie['id'])

            if Movie.objects.filter(id=movie['id']).exists():
                movie_update : Movie = Movie.objects.get(id=movie['id'])
                movie_update.convert_json_to_object(json)
                movie_update.save()
            else:
                movie_update : Movie = Movie()
                movie_update.convert_json_to_object(json)
                movie_update.save()
            

def update_now_playing_movies():
    '''
    Get the first five pages now playing movies from TMDB and save them in the database
    If a movie already exists in the database, update it
    '''
    for i in range(1,6):
        movies = tmdb_movie()
        movies = movies.now_playing(language='fr', page=i)
        for movie in movies['results']:
            json = get_detail_from_id(movie['id'])

            if Movie.objects.filter(id=movie['id']).exists():
                movie_update : Movie = Movie.objects.get(id=movie['id'])
                movie_update.convert_json_to_object(json)
                movie_update.save()
            else:
                movie_update : Movie = Movie()
                movie_update.convert_json_to_object(json)
                movie_update.save()

def get_detail_from_id(id) -> dict:
    '''
    Get details of movies on database and save them
    '''
    movie_details = tmdb_movie(id)
    movie_details = movie_details.detail(language='fr')

    return movie_details

def run():
    update_top_rated_movies()
    update_popular_movies()
    update_upcoming_movies()
    update_now_playing_movies()

    # update_movies_details()