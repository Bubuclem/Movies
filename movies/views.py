# Django
# ==========
from unittest import result
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

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

        list_movies = []
        for movie in movies_now_playing['results']:
            list_movies.append(movie)

        return render(request, 'gallery/gallery.html', {'list_movies':list_movies})

class MovieDetailView(BaseView):
    def get(self,request,movie_id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        movie = tmdb.Movies(movie_id)
        response = movie.info(language='fr')
        
        return render(request, 'content/content.html', {'movie':response})

class TVView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        tv = tmdb.TV()
        medias_now_playing = tv.on_the_air()

        list_tv = []
        for movie in medias_now_playing['results']:
            list_tv.append(movie)

        return render(request, 'gallery/gallery.html', {'list_tv':list_tv})

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

        list_peoples = []
        for people in peoples_popular['results']:
            list_peoples.append(people)

        return render(request, 'gallery/gallery.html', {'list_peoples':list_peoples})

class PeoplesDetailView(BaseView):
    def get(self,request,people_id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        people = tmdb.People(people_id)
        response = people.info(language='fr')
        
        return render(request, 'content/content.html', {'people':response})

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