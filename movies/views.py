# Django
# ==========
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

# API
# ===
#from .serializers import MoviesSerializer
#from rest_framework import viewsets
#from rest_framework import permissions

# Imports
# ==========
import tmdbsimple as tmdb
import requests

# Class Base
# ==========
class BaseView(TemplateView):
            
    tmdb.API_KEY = settings.SECRET_KEY_TMDB
    tmdb.REQUESTS_SESSION = requests.Session()

    def isNotauthenticated(self,request) -> bool :
        if request.user.is_authenticated:
            return True
        return False

    def isStaff(self,request) -> bool:
        return request.user.is_staff

# Class Views
# ===========
class MediaView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')
        return render(request, 'gallery/gallery.html', {})

class MoviesView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        movies = tmdb.Movies()
        movies_now_playing = movies.now_playing()

        return render(request, 'gallery/gallery.html', {'list_movies':movies_now_playing['results']})

    def post(self, request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        _page = request.POST['page']

        movies = tmdb.Movies()
        movies_now_playing = movies.now_playing(page=_page)

        return render(request, 'gallery/gallery.html', {'list_movies':movies_now_playing['results']})

class MovieDetailView(BaseView):
    def get(self,request,movie_id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        movie = tmdb.Movies(movie_id)
        response = movie.info(language='fr')
        
        videos = movie.videos(language='fr')

        return render(request, 'content/content.html', { 'movie':response, 'videos':videos['results'] })

class TVView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        tv = tmdb.TV()
        medias_now_playing = tv.on_the_air()

        return render(request, 'gallery/gallery.html', {'list_tv':medias_now_playing['results']})

class TVDetailView(BaseView):
    def get(self,request,tv_id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        movie = tmdb.TV(tv_id)
        response = movie.info(language='fr')
        
        return render(request, 'content/content.html', {'tv':response})

class GenresView(BaseView):
    def get(self,request):
        self.isNotauthenticated()

class PeoplesView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        peoples = tmdb.People()
        peoples_popular = peoples.popular()

        return render(request, 'gallery/gallery.html', {'list_peoples':peoples_popular['results']})

class PeoplesDetailView(BaseView):
    def get(self,request,people_id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        people = tmdb.People(people_id)
        response = people.info(language='fr')
        
        populars = people.popular(language='fr')

        return render(request, 'content/content.html', {'people':response, 'list_populars':populars['results'][0]['known_for']})

class VideosView(BaseView):
    def get(self,request):
        self.isNotauthenticated()

class AccountView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')
        return render(request, 'form/form.html', {})

class UsersView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False and self.isStaff() == False:
           pass

class SearchView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
           return HttpResponseRedirect('/login')
        return render(request, 'gallery/gallery.html', {})

    def post(self, request):
        _search = request.POST['search']
        search = tmdb.Search()
        response = search.multi(query=_search)

        results = []
        for res in response['results']:
            results.append(res)

        return render(request, 'gallery/gallery.html', {'results':results})

class LoginView(BaseView):
    def get(self,request):
        return render(request, 'form/login.html', {})

    def post(self,request):
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(request,username=_username,password=_password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'form/login.html', {})

class LogoutView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')
        logout(request)
        return HttpResponseRedirect ('/login')

# API
# ===

