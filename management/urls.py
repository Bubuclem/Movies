from django.urls import path

from .views import LoginView, LogoutView

app_name = 'management'
urlpatterns = [
    # URL de connexion
    path('authentification/', 
    LoginView.as_view(), 
    name='login'),

    # URL de connexion
    path('deconnexion/', 
    LogoutView.as_view(), 
    name='logout'),
]