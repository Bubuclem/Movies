from django.urls import path

from . import views

app_name = 'actors'
urlpatterns = [
    # Actors - Page principal
    # =====
    path('', 
    views.ActorsView.as_view(), 
    name='actors'),

    # URL Actors - Page
    path('/<int:page>', 
    views.ActorsView.as_view(), 
    name='actors'),

    # URL Actor détail
    path('/<int:actor_id>', 
    views.ActorDetailView.as_view(), 
    name='actor-detail'),

    # URL Actor
    path('/<int:actor_id>/images', 
    views.ActorImagesView.as_view(), 
    name='actor-images')
]