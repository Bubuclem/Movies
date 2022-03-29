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
from .tmdb import Movies, TV, Search, People

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

class MoviesView(BaseView):
    def get(self,request,page=None):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        movies = Movies()
        movies_now_playing = movies.popular(language='fr',page=page)

        return render(request, 'pages/mediaview/medias.html', { 'movies':movies_now_playing['results'], 'total_pages':movies_now_playing['total_pages'] })

class MovieDetailView(BaseView):
    def get(self,request,movie_id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        movie = Movies(movie_id)
        response = movie.detail(language='fr')
        
        credits = movie.credits()
        videos = movie.videos(language='fr')
        reviews = movie.reviews(language='fr')

        return render(request, 'pages/mediaview/media.html', { 'movie':response, 'credits':credits['cast'][:8], 'videos':videos['results'][:4], 'reviews':reviews['results'] })

class TVView(BaseView):
    def get(self,request,page=None):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        tv = TV()
        medias_now_playing = tv.popular(language='fr',page=page)

        return render(request, 'pages/mediaview/medias.html', {'shows':medias_now_playing['results'], 'total_pages':medias_now_playing['total_pages'] })

class TVDetailView(BaseView):
    def get(self,request,tv_id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        media = TV(tv_id)
        response = media.detail(language='fr')
        
        return render(request, 'pages/mediaview/media.html', {'tv':response})

class GenresView(BaseView):
    def get(self,request):
        self.isNotauthenticated()

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

        return render(request, 'pages/mediaview/media.html', {'people':response, 'list_populars':populars['results'][0]['known_for']})

class PeopleImagesView(BaseView):
    def get(self,request,people_id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')

        people = People(people_id)
        response = people.detail(language='fr')
        
        images = people.images()

        return render(request, 'pages/peoplesview/images.html', {'people':response, 'images':images['profiles'] })

class VideosView(BaseView):
    def get(self,request):
        self.isNotauthenticated()

class AccountView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')
        return render(request, 'pages/accountview/account.html', {})

class UsersView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False and self.isStaff() == False:
           pass

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

