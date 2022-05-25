from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, AccountForm, RegistreAccountForm
from movies.views import PopularPageView

TEMPLATE_BASE = 'pages/management/'

class LoginPageView(TemplateView):
    '''
    Class des connexions.
    Retourne la page de connexion
    '''
    template_name = TEMPLATE_BASE + 'login/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        return context

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

class LogoutPageView(TemplateView):
    '''
    Class des déconnexion.
    Retourne la page de déconnexion
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