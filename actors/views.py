from django.shortcuts import render
from django.views.generic import TemplateView

from ESGI_Movies.wrappe.tmdb import tmdb_people

# Class Actors
# ===========
class ActorsView(TemplateView):
    def get(self,request,page=None):
        peoples = tmdb_people()
        peoples_popular = peoples.popular(page=page)

        return render(request, 'pages/peoplesview/peoples.html', { 'peoples':peoples_popular['results'], 'total_pages':peoples_popular['total_pages'] })

class ActorDetailView(TemplateView):
    def get(self,request,people_id):
        people = tmdb_people(people_id)
        response = people.detail(language='fr')
        
        populars = people.popular(language='fr')

        return render(request, 'pages/peoplesview/people.html', {'people':response, 'list_populars':populars['results'][0]['known_for']})

class ActorImagesView(TemplateView):
    def get(self,request,people_id):
        people = tmdb_people(people_id)
        response = people.detail(language='fr')
        
        images = people.images()

        return render(request, 'pages/peoplesview/images.html', {'people':response, 'images':images['profiles'] })
# ===========