from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from management.forms import LoginForm, AccountForm, RegistreAccountForm
from management.models import Watched, Favorite
from movies.models import Movie
from shows.models import Show

TEMPLATE_BASE = 'pages/management/'

''''
Connexion class
'''
class LoginPageView(TemplateView):
    '''
    Method Get login page
    if user is logged, redirect to the class view of the popular movies
    return connexion page with form
    '''
    template_name = TEMPLATE_BASE + 'login/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        return context

    '''
    Method Post login page
    return to the main page /popular if the connexion is ok
    '''
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data['email'].lower())
            except User.DoesNotExist:
                return redirect('/vitrine/authentification/')

            user = authenticate(self.request, username=user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/films/populaires/')
        return redirect('/authentification/')

''''
Logout class
'''
class LogoutPageView(TemplateView):
    '''
    Method Get logout page
    logout the user and return to the login page
    '''
    template_name = TEMPLATE_BASE + 'logout/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logout(self.request)

        return context

class RegisterAccountPageView(TemplateView):
    '''
    Class de création de compte.
    Retourne le formulaire d'inscription
    '''
    template_name = TEMPLATE_BASE + 'register/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegistreAccountForm()
        return context

class AccountPageView(TemplateView):
    '''
    Class du profil utilisateur.
    Retourne le formulaire du profile utilisateur
    '''
    template_name = TEMPLATE_BASE + 'account/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AccountForm()
        return context

class SuccesPageView(View):
    def get(self, request):
        return render(request,'generic/succes.html',{})

class WatchlistPageView(ListView):
    '''
    Class de la page watchlist.
    Retourne la liste des films de la watchlist
    '''
    template_name = TEMPLATE_BASE + 'account/watchlist.html'
    context_object_name = 'watched'
    paginate_by = 10

    def get_queryset(self):
        return Watched.objects.filter(user=self.request.user).order_by('pub_date')

class FavoritesPageView(ListView):
    '''
    Class de la page favoris.
    Retourne la liste des films des favoris.
    '''
    template_name = TEMPLATE_BASE + 'account/favoris.html'
    context_object_name = 'favoris'
    paginate_by = 10

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).order_by('pub_date')

class MoviesPageView(ListView):
    '''
    Class : Movies list
    Description : Manage movies
    '''
    template_name = TEMPLATE_BASE + 'back/movies.html'
    model = Movie
    paginate_by = 15
    context_object_name = 'movies'

class MoviePageView(DetailView):
    '''
    Class : Detail view for movie
    Description : Edit movie
    '''
    template_name = TEMPLATE_BASE + 'back/movie.html'

    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ShowsPageView(ListView):
    '''
    Class : Shows list
    Description : Manage shows
    '''
    template_name = TEMPLATE_BASE + 'back/shows.html'
    model = Show
    paginate_by = 15
    context_object_name = 'shows'

class ShowPageView(DetailView):
    '''
    Class : Detail view for show
    Description : Edit show
    '''
    template_name = TEMPLATE_BASE + 'back/show.html'

    model = Show

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context