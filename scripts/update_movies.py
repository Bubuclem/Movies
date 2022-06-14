from movies.models import Movie
from management.models import Crew, Cast, Credit
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

def update_movies_details():
    '''
    Get details of movies on database and save them
    '''
    movies = Movie.objects.all()
    for movie in movies:
        movie_details = tmdb_movie(movie.id)
        movie_details = movie_details.detail()

        movie.runtime = movie_details['runtime']
        movie.revenue = movie_details['revenue']
        movie.budget = movie_details['budget']
        movie.status = movie_details['status']

        movie.save()

        '''
        Get credits of movies on database and save them
        '''
        movie_credits = tmdb_movie(movie.id)
        movie_credits = movie_credits.credits()

        cast_ids = []

        for cast in movie_credits['cast']:

            cast_ids.append(cast['id'])

            if Cast.objects.filter(id=cast['id']).exists() is False:
                Cast.objects.create(
                    id=cast['id'],
                    name=cast['name'],
                    known_for_department=cast['known_for_department'],
                    character=cast['character'],
                    order=cast['order'],
                    profile_path=cast['profile_path'],
                    original_name=cast['original_name'],
                    popularity=cast['popularity'],
                    credit_id=cast['credit_id'],
                    gender=cast['gender'],
                    cast_id=cast['cast_id']
                )
            else:
                cast_update : Cast = Cast.objects.get(id=cast['id'])
                cast_update.name=cast['name']
                cast_update.known_for_department=cast['known_for_department']
                cast_update.character=cast['character']
                cast_update.order=cast['order']
                cast_update.profile_path=cast['profile_path']
                cast_update.original_name=cast['original_name']
                cast_update.popularity=cast['popularity']
                cast_update.credit_id=cast['credit_id']
                cast_update.gender=cast['gender']
                cast_update.cast_id=cast['cast_id']
                cast_update.save()

        crew_ids = []

        for crew in movie_credits['crew']:

            crew_ids.append(crew['id'])

            if Crew.objects.filter(id=crew['id']).exists() is False:
                Crew.objects.create(
                    id=crew['id'],
                    name=crew['name'],
                    job=crew['job'],
                    profile_path=crew['profile_path'],
                    department=crew['department'],
                    original_name=crew['original_name'],
                    popularity=crew['popularity'],
                    credit_id=crew['credit_id'],
                    gender=crew['gender']
                )
            else:
                crew_update : Crew = Crew.objects.get(id=crew['id'])
                crew_update.name=crew['name']
                crew_update.job=crew['job']
                crew_update.profile_path=crew['profile_path']
                crew_update.department=crew['department']
                crew_update.original_name=crew['original_name']
                crew_update.popularity=crew['popularity']
                crew_update.credit_id=crew['credit_id']
                crew_update.gender=crew['gender']
                crew_update.save()

        for credit in movie_credits:

            list_cast = Credit.objects.filter(id__in=cast_ids)
            list_crew = Credit.objects.filter(id__in=crew_ids)

            if Credit.objects.filter(id=movie_credits['id']).exists() is False:
                Credit.objects.create(
                    id=movie_credits['id'],
                    media_type='movie'
                )
            else:
                credit_update :Credit = Credit.objects.get(id=movie_credits['id'])
                credit_update.media_type='movie'
                credit_update.cast.set(list_cast)
                credit_update.crew.set(list_crew)
                credit_update.save()

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