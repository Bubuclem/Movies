# Django
# ==========
from turtle import title
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

# API
# ===
from .serializers import MovieSerializer, ShowSerializer
from rest_framework import viewsets
from rest_framework import permissions

# Imports
# ==========
from .tmdb import tmdb_movie, tmdb_tv, Search, People
from .models import Movie, Show

# Class Base
# ==========
class BaseView(TemplateView):
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
        return render(request, 'pages/indexview/index.html', {})

# Class Movies
# ===========
class MoviesView(BaseView):
    def get(self,request,page=None,type=""):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        movies = tmdb_movie()

        if type=="": # Populaire
            medias = movies.popular(language='fr',page=page)
        elif type=="mieux-notés": # Mieux notées
            medias = movies.top_rated(language='fr',page=page)
        elif type=="en-cours-de-diffusion":
            medias = movies.now_playing(language='fr',page=page)

        return render(request, 'pages/mediaview/medias.html', { 'movies':medias['results'], 'total_pages':medias['total_pages'] })

class MovieDetailView(BaseView):
    def get(self,request,movie_id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        movies  = tmdb_movie(movie_id)
        movie   = movies.detail(language='fr')
        
        credits = movies.credits()
        videos  = movies.videos(language='fr')
        reviews = movies.reviews(language='fr')

        return render(request, 'pages/mediaview/media.html', { 'media':movie, 'credits':credits['cast'][:8], 'videos':videos['results'][:4], 'reviews':reviews['results'] })
# ===========

# Class Shows
# ===========
class TVView(BaseView):
    def get(self,request,page=None,type=""):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        tv = tmdb_tv()

        if type=="": # Populaire
            shows = tv.popular(language='fr',page=page)
        elif type=="mieux-notées": # Mieux notées
            shows = tv.top_rated(language='fr',page=page)
        elif type=="en-cours-de-diffusion":
            shows = tv.on_the_air(language='fr',page=page)

        return render(request, 'pages/mediaview/medias.html', {'shows':shows['results'], 'total_pages':shows['total_pages'] })

class TVDetailView(BaseView):
    def get(self,request,tv_id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        media = tmdb_tv(tv_id)
        response = media.detail(language='fr')
        
        credits = media.credits()
        videos = media.videos(language='fr')
        reviews = media.reviews(language='fr')

        return render(request, 'pages/mediaview/media.html', {'media':response, 'credits':credits['cast'][:8], 'videos':videos['results'][:4], 'reviews':reviews['results']})
# ===========

# Class Peoples
# ===========
class PeoplesView(BaseView):
    def get(self,request,page=None):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        peoples = People()
        peoples_popular = peoples.popular(page=page)

        return render(request, 'pages/peoplesview/peoples.html', { 'peoples':peoples_popular['results'], 'total_pages':peoples_popular['total_pages'] })

class PeopleDetailView(BaseView):
    def get(self,request,people_id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        people = People(people_id)
        response = people.detail(language='fr')
        
        populars = people.popular(language='fr')

        return render(request, 'pages/peoplesview/people.html', {'people':response, 'list_populars':populars['results'][0]['known_for']})

class PeopleImagesView(BaseView):
    def get(self,request,people_id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        people = People(people_id)
        response = people.detail(language='fr')
        
        images = people.images()

        return render(request, 'pages/peoplesview/images.html', {'people':response, 'images':images['profiles'] })
# ===========

# Class Videos
# ===========
class VideosView(BaseView):
    def get(self,request):
        self.isNotauthenticated()
# ===========

# Class Account
# ===========
class AccountView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')
        return render(request, 'pages/accountview/account.html', {})
# ===========

# Class Search
# ===========
class SearchView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
           return HttpResponseRedirect('/login')
        return render(request, 'pages/mediaview/medias.html', {})

    def post(self, request):
        _search = request.POST['search']
        search = Search()
        response = search.multi(query=_search)

        results = []
        for res in response['results']:
            results.append(res)

        return render(request, 'pages/mediaview/medias.html', {'results':results})
# ===========

class LoginView(BaseView):
    def get(self,request):
        return render(request, 'pages/loginview/login.html', {})

    def post(self,request):
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(request,username=_username,password=_password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'pages/loginview/login.html', {})

class LogoutView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')
        logout(request)
        return HttpResponseRedirect ('/login')

# API
# ===

class MovieViewSet(viewsets.ModelViewSet):
    movies = tmdb_movie()
    medias = movies.popular(language='fr')

    for movie in medias['results']:
        Movie.objects.create(movie_id=movie['id'],title=movie['title'],poster_path=movie['poster_path'],overview=movie['overview'],release_date=movie['release_date'],original_title=movie['original_title'],original_language=movie['original_language'],backdrop_path=movie['backdrop_path'],popularity=movie['popularity'],vote_count=movie['vote_count'],vote_average=movie['vote_average'],adult=movie['adult'])

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShowViewSet(viewsets.ModelViewSet):
    shows = tmdb_tv()
    medias = shows.popular(language='fr')

    for media in medias['results']:
        Show.objects.create(tv_id=media['id'],name=media['name'],poster_path=media['poster_path'],overview=media['overview'],original_name=media['original_name'],original_language=media['original_language'],backdrop_path=media['backdrop_path'],popularity=media['popularity'],vote_count=media['vote_count'],vote_average=media['vote_average'])

    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    permission_classes = [permissions.IsAuthenticated]