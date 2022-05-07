from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, AccountForm, RegistreAccountForm

TEMPLATE_BASE = 'pages/management/'

# Class de connexion
# ===========
class LoginPageView(TemplateView):

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

# Class de déconnexion
# ===========
class LogoutPageView(TemplateView):

    template_name = TEMPLATE_BASE + 'logout/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logout(self.request)

        return context

# Class de création de compte
class RegisterAccountPageView(TemplateView):
    
    template_name = TEMPLATE_BASE + 'register/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegistreAccountForm()
        return context

# Class du profil utilisateur
class AccountPageView(TemplateView):
    
    template_name = TEMPLATE_BASE + 'account/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AccountForm()
        return context