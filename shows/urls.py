from django.urls import path

from . import views

app_name = 'shows'
urlpatterns = [    
    # Shows - Page principal
    # =====
    path('', 
    views.ShowsView.as_view(), 
    name='shows'),

    # URL Séries - Type
    path('/<str:type>', 
    views.ShowsView.as_view(), 
    name='shows'),

    # URL Séries - Populaire - Page
    path('/<int:page>', 
    views.ShowsView.as_view(), 
    name='shows'),

    # URL Séries - Type - Page
    path('/<int:page>/<str:type>', 
    views.ShowsView.as_view(), 
    name='shows'),

    # URL Série détail
    path('/<int:tv_id>', 
    views.ShowDetailView.as_view(), 
    name='show-detail')
]