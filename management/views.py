from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm

from management.forms import LoginForm, AccountForm, RegistreAccountForm, ReviewForm
from management.models import Review, Watched, Favorite
from movies.models import Movie
from shows.models import Show

TEMPLATE_BASE = 'pages/management/'

''''
Connexion class
'''
class LoginPageView(FormView):
    template_name = TEMPLATE_BASE + 'auth/login.html'
    form_class = LoginForm
    success_url = '/films/populaires/'

    def form_valid(self, form):
        try:
            user = User.objects.get(email=form.cleaned_data['email'])
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(self.request, user)
                return super().form_valid(form)
        except User.DoesNotExist:
            return render(self.request, self.template_name, {'form': form, 'error': 'Email does not exist'})

class LogoutPageView(TemplateView):
    ''' 
    Logout page
    '''
    template_name = TEMPLATE_BASE + 'auth/logout.html'

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

class AccountPageView(FormView):
    '''
    Class de gestion du compte.
    Retourne le formulaire de modification de compte
    '''
    template_name = TEMPLATE_BASE + 'account/account.html'
    form_class = AccountForm
    success_url = '/profile/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AccountForm(instance=self.request.user)
        return context

    def post(self, request):
        form = AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile/')

class ReviewsPageView(ListView):
    '''
    Class de gestion des avis.
    '''
    template_name = TEMPLATE_BASE + 'account/reviews.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user).order_by('-pub_date')

class ReviewsDetailPageView(DetailView):
    '''
    Class d'édition d'un avis.
    '''
    template_name = TEMPLATE_BASE + 'account/review.html'
    model = Review
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm(instance=self.object)
        return context

    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review.content = form.cleaned_data['content']
            review.save()
            return redirect('/avis/')

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
        return Watched.objects.filter(user=self.request.user).order_by('-pub_date')

class FavoritesPageView(ListView):
    '''
    Class de la page favoris.
    Retourne la liste des films des favoris.
    '''
    template_name = TEMPLATE_BASE + 'account/favoris.html'
    context_object_name = 'favoris'
    paginate_by = 10

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).order_by('-pub_date')

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

class PasswordPageView(FormView):
    '''
    Class : Password change
    Description : Change password
    '''
    template_name = TEMPLATE_BASE + 'account/password.html'
    form_class = PasswordChangeForm
    success_url = '/profile/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PasswordChangeForm(instance=self.request.user)
        return context

class UserManagementPageView(ListView):
    '''
    Class : User management
    Description : Manage users
    '''
    template_name = TEMPLATE_BASE + 'account/users.html'
    model = User
    paginate_by = 15
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all().order_by('-date_joined')