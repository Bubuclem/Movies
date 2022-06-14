from shows.models import Show
from ESGI_Movies.wrappe.tmdb import tmdb_tv

def update_top_rated_shows():
    '''
    Get the first five pages top rated shows from TMDB and save them in the database
    '''
    for i in range(1,6):
        shows = tmdb_tv()
        shows = shows.top_rated(language='fr', page=i)
        for show in shows['results']:
            json = get_detail_from_id(show['id'])

            if Show.objects.filter(id=show['id']).exists():
                show_update : Show = Show.objects.get(id=show['id'])
                show_update.convert_json_to_object(json)
                show_update.save()
            else:
                show_update : Show = Show()
                show_update.convert_json_to_object(json)
                show_update.save()

def update_popular_shows():
    '''
    Get the first five pages popular shows from TMDB and save them in the database
    '''
    for i in range(1,6):
        shows = tmdb_tv()
        shows = shows.popular(language='fr', page=i)
        for show in shows['results']:
            json = get_detail_from_id(show['id'])

            if Show.objects.filter(id=show['id']).exists():
                show_update : Show = Show.objects.get(id=show['id'])
                show_update.convert_json_to_object(json)
                show_update.save()
            else:
                show_update : Show = Show()
                show_update.convert_json_to_object(json)
                show_update.save()

def update_upcoming_shows():
    '''
    Get the first five pages upcoming movies from TMDB and save them in the database
    '''
    for i in range(1,6):
        shows = tmdb_tv()
        shows = shows.on_the_air(language='fr', page=i)
        for show in shows['results']:
            json = get_detail_from_id(show['id'])

            if Show.objects.filter(id=show['id']).exists():
                show_update : Show = Show.objects.get(id=show['id'])
                show_update.convert_json_to_object(json)
                show_update.save()
            else:
                show_update : Show = Show()
                show_update.convert_json_to_object(json)
                show_update.save()

def update_on_the_air_shows():
    '''
    Get the first five pages now playing movies from TMDB and save them in the database
    '''
    for i in range(1,6):
        shows = tmdb_tv()
        shows = shows.on_the_air(language='fr', page=i)
        for show in shows['results']:
            json = get_detail_from_id(show['id'])

            if Show.objects.filter(id=show['id']).exists():
                show_update : Show = Show.objects.get(id=show['id'])
                show_update.convert_json_to_object(json)
                show_update.save()
            else:
                show_update : Show = Show()
                show_update.convert_json_to_object(json)
                show_update.save()

def get_detail_from_id(id) -> dict:
    '''
    Get details of tv show on database and save them
    '''
    show_details = tmdb_tv(id)
    show_details = show_details.detail(language='fr')

    return show_details

def run():
    update_top_rated_shows()
    update_popular_shows()
    update_upcoming_shows()
    update_on_the_air_shows()