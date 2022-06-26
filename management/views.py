from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.conf import settings

from management.forms import LoginForm, AccountForm, RegistreAccountForm, ReviewForm, UserForm, ChangePasswordForm, RequestApiForm
from management.models import Review, Watched, Favorite, RequestApi
from movies.models import Movie
from shows.models import Show

TEMPLATE_BASE = 'pages/management/'

class LoginPageView(FormView):
    ''''
    Vue pour la page de connexion.
    '''
    template_name = TEMPLATE_BASE + 'auth/login.html'
    form_class = LoginForm
    success_url = '/films/populaires/'

    def form_valid(self, form):
        try:
            user = User.objects.get(email=form.cleaned_data['email'])
            auth = authenticate(username=user.username, password=form.cleaned_data['password'])
            if auth is not None and auth.is_active:
                login(self.request, auth)
                return super().form_valid(form)
            elif user.is_active is False:
                error='Votre compte est désactivé'
            elif auth is None:
                error='Les informations fournies ne correspondent à aucun compte.'
        except User.DoesNotExist:
            pass

        return render(self.request, self.template_name, {'form': form, 'error': error})

class LogoutPageView(TemplateView):
    ''' 
    Vue de déconnexion de l'utilisateur courant.
    '''
    template_name = TEMPLATE_BASE + 'auth/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logout(self.request)

        return context

class RegisterAccountPageView(TemplateView):
    '''
    Vue pour la page d'inscription.
    '''
    template_name = TEMPLATE_BASE + 'register/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegistreAccountForm()
        return context

class AccountPageView(FormView):
    '''
    Vue pour la page de profil.
    '''
    template_name = TEMPLATE_BASE + 'account/account.html'
    form_class = AccountForm
    success_url = '/dashboard/profile/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AccountForm(instance=self.request.user)
        return context

    def post(self, request):
        form = AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)

class ReviewsPageView(ListView):
    '''
    Vue pour la page des commentaires.
    '''
    template_name = TEMPLATE_BASE + 'account/reviews.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user).order_by('-pub_date')

class ReviewsDetailPageView(DetailView):
    '''
    Vue pour la page de détails d'un commentaire.
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
    Vue pour la page de la watchlist.
    '''
    template_name = TEMPLATE_BASE + 'account/watchlist.html'
    context_object_name = 'watched'
    paginate_by = 10

    def get_queryset(self):
        return Watched.objects.filter(user=self.request.user).order_by('-pub_date')

class FavoritesPageView(ListView):
    '''
    Vue pour la page des favoris.
    '''
    template_name = TEMPLATE_BASE + 'account/favoris.html'
    context_object_name = 'favoris'
    paginate_by = 10

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).order_by('-pub_date')

class MoviesPageView(ListView):
    '''
    Vue pour la page des films.
    '''
    template_name = TEMPLATE_BASE + 'back/movies.html'
    model = Movie
    paginate_by = 15
    context_object_name = 'movies'

class MoviePageView(DetailView):
    '''
    Vue pour la page d'un film.
    '''
    template_name = TEMPLATE_BASE + 'back/movie.html'

    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ShowsPageView(ListView):
    '''
    Vue pour la page des séries.
    '''
    template_name = TEMPLATE_BASE + 'back/shows.html'
    model = Show
    paginate_by = 15
    context_object_name = 'shows'

class ShowPageView(DetailView):
    '''
    Vue pour la page d'une série.
    '''
    template_name = TEMPLATE_BASE + 'back/show.html'

    model = Show

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PasswordPageView(TemplateView):
    '''
    Vue pour modifier le mot de passe de l'utilisateur connecté.
    '''
    template_name = TEMPLATE_BASE + 'account/password.html'
    form_class = ChangePasswordForm
    success_url = 'dashboard/securite/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ChangePasswordForm(self.request.user)
        return context

    def post(self, request):
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'form': form, 'message': 'Mot de passe modifié avec succès.'})
        return render(request, self.template_name, {'form': form, 'message': 'Les informations fournies ne correspondent pas.'})

class RequestApiPageView(TemplateView):
    '''
    Vue pour la page de demande d'API.
    '''
    template_name = TEMPLATE_BASE + 'account/api.html'
    form_class = RequestApiForm
    success_url = 'dashboard/securite/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            api: RequestApi = RequestApi.objects.get(user=self.request.user)
        except RequestApi.DoesNotExist:
            api = None

        if api and api.enable:
            try:
                context['token'] = Token.objects.get(user=api.user)
            except Token.DoesNotExist:
                context['token'] = Token.objects.create(user=api.user)
        elif api and api.enable is False:
            context['message'] = 'Votre demande n\'a pas encore été traitée.'
        else:
            context['form'] = RequestApiForm()

        return context

    def post(self, request):
        form = RequestApiForm(request.POST)
        if form.is_valid():
            requestAPI = form.save()

            requestAPI.user_id = request.user.id
            requestAPI.save()

            return render(request, self.template_name, {'form': form, 'message': 'Demande de clé API envoyée avec succès.'})
        return render(request, self.template_name, {'form': form, 'message': 'Les informations fournies ne correspondent pas.'})

class InboxRequestApiPageView(ListView):
    '''
    Vue pour la page de demande d'API.
    '''
    template_name = TEMPLATE_BASE + 'account/requestapi.html'
    model = RequestApi
    context_object_name = 'requests'
    paginate_by = 10

    def get_queryset(self):
        return RequestApi.objects.all().order_by('-pub_date')

    def post(self, request):
        requestAPI = RequestApi.objects.get(pk=request.POST['id'])
        requestAPI.enable = not requestAPI.enable
        requestAPI.save()
        return redirect('/dashboard/boite-de-reception/')

class UserManagementPageView(ListView):
    '''
    Vue pour la gestion des utilisateurs, triée par date de création.
    '''
    template_name = TEMPLATE_BASE + 'account/users.html'
    model = User
    paginate_by = 15
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all().order_by('-date_joined')

class UserManagementDetailPageView(FormView):
    '''
    Vue pour la gestion d'un utilisateur.
    '''
    template_name = TEMPLATE_BASE + 'account/user.html'
    form_class = UserForm
    success_url = '/dashboard/utilisateurs/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.kwargs['pk'] == 'nouveau':
            context['form'] = UserForm()
        else:
            context['form'] = UserForm(instance=User.objects.get(pk=self.kwargs['pk']))
            context['id'] = self.kwargs['pk']
        return context
 
    def post(self, request, pk):
        if pk == 'nouveau':
            form = UserForm(request.POST)
        else :
            form = UserForm(request.POST, instance=User.objects.get(pk=pk))
        if form.is_valid():
            form.save()
        return redirect(self.success_url)

class ActiveUserPageView(View):
    '''
    Vue pour activer/desactiver un utilisateur.
    '''
    def get(self, request, pk):
        try :
            user : User = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return redirect('/dashboard/utilisateurs/')
        user.is_active = not user.is_active
        user.save()
        return redirect('/dashboard/utilisateurs/')

class EmailTestPageView(TemplateView):
    '''
    Vue pour tester l'envoi d'un email.
    '''
    template_name = TEMPLATE_BASE + 'account/emailtest.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request):
        send_mail(
            'Subject here',
            'Here is the message.',
            '{}'.format(settings.EMAIL_HOST_USER),
            [request.POST['email']],
            fail_silently=False,
        )