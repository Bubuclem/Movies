from django.urls import path

from .views import LoginPageView, LogoutPageView, RegisterAccountPageView,AccountPageView

app_name = 'management'
urlpatterns = [
    # URL de connexion
    path('', 
    LoginPageView.as_view(), 
    name='login'),

    # URL de connexion
    path('authentification/', 
    LoginPageView.as_view(), 
    name='login'),

    # URL de déconnexion
    path('deconnexion/', 
    LogoutPageView.as_view(), 
    name='logout'),
    
    # URL de création de compte
    path('nouveau-compte/', 
    RegisterAccountPageView.as_view(), 
    name='register'),

    # URL du profile utilisateur
    path('profile/', 
    AccountPageView.as_view(), 
    name='account'),
]