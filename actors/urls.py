from django.urls import path

from .views import PopularPageView, ActorPageView, SearchPageView

app_name = 'actors'
urlpatterns = [
    # URL des acteurs populaires
    path('populaires/', 
    PopularPageView.as_view(), 
    name='popular'),

    # URL de recherche d'acteurs
    path('recherche/',
    SearchPageView.as_view(),
    name='search'),

    # URL du détail d'un acteur
    path('<int:actor_id>/', 
    ActorPageView.as_view(), 
    name='detail'),
]