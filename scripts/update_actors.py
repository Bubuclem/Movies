from actors.models import Actor
from ESGI_Movies.wrappe.tmdb import tmdb_people

'''
Get the first five pages of popular actors in french from TMDB and save them in the database
'''
def update_popular_actors():
    for page in range(1, 6):
        actors = tmdb_people()
        actors = actors.popular(language='fr',page=page)
        for actor in actors['results']:
            json = get_detail_from_id(actor['id'])
            
            if Actor.objects.filter(id=actor['id']).exists():
                actor_update : Actor = Actor.objects.get(id=actor['id'])
                actor_update.convert_json_to_object(json)
                actor_update.save()
            else:
                actor_update : Actor = Actor()
                actor_update.convert_json_to_object(json)
                actor_update.save()

def get_detail_from_id(id) -> dict:
    '''
    Get details of actor on database and save them
    '''
    actor_details = tmdb_people(id)
    actor_details = actor_details.detail(language='fr')

    return actor_details

def run():
    update_popular_actors()