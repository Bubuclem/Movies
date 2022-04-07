from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

from ESGI_Movies.wrappe.tmdb import tmdb_movie, tmdb_search, tmdb_genres

# Class Base
# ==========
class BaseView(TemplateView):
    def isNotauthenticated(self,request) -> bool :
        return request.user.is_authenticated

    def isStaff(self,request) -> bool:
        return request.user.is_staff

# Class Movies
# ===========
class MoviesView(BaseView):
    def get(self,request,page=None,type=""):
        movies = tmdb_movie()

        if type=="": # Populaire
            medias = movies.popular(language='fr',page=page)
        elif type=="mieux-notés": # Mieux notées
            medias = movies.top_rated(language='fr',page=page)
        elif type=="en-cours-de-diffusion":
            medias = movies.now_playing(language='fr',page=page)

        genres = tmdb_genres()

        return render(request, 'pages/mediaview/medias.html', { 'movies':medias['results'], 'total_pages':medias['total_pages'], 'genres':genres })

class MovieDetailView(BaseView):
    def get(self,request,movie_id):
        movies  = tmdb_movie(movie_id)
        movie   = movies.detail(language='fr')
        
        credits = movies.credits()
        videos  = movies.videos(language='fr')
        reviews = movies.reviews(language='fr')

        return render(request, 'pages/mediaview/media.html', { 'media':movie, 'credits':credits['cast'][:8], 'videos':videos['results'][:4], 'reviews':reviews['results'] })
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
        return render(request, 'pages/mediaview/medias.html', {})

    def post(self, request):
        _search = request.POST['search']
        search = tmdb_search()
        response = search.multi(query=_search)

        results = []
        for res in response['results']:
            results.append(res)

        return render(request, 'pages/mediaview/medias.html', {'results':results})
# ===========

# Class Login
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
# ===========

# Class Logout
# ===========
class LogoutView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')
        logout(request)
        return HttpResponseRedirect ('/login')
# ===========

# API
# ===
# from rest_framework import viewsets
# from rest_framework import views
# from rest_framework.response import Response
# 
# from .serializers import MovieSerializer, ShowSerializer, shows

# class ShowsViewSet(viewsets.ViewSet):
#     
#     serializer_class = ShowSerializer
# 
#     def list(self, request):
#         serializer = ShowSerializer(
#             instance=shows.values(), many=True)
#         return Response(serializer.data)