from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'popular-movies', views.MoviesPopularViewSet,basename='popular-movies')
router.register(r'top-rated-movies', views.MoviesTopRatedViewSet,basename='top-rated-movies')
router.register(r'upcoming-movies', views.MoviesUpcomingViewSet,basename='upcoming-movies')
router.register(r'now-playing-movies', views.MoviesNowPlayingViewSet,basename='now-playing-movies')
router.register(r'lastest-movies', views.MoviesLastestViewSet,basename='lastest-movies')
router.register(r'movie', views.MovieViewSet,basename='movie')
router.register(r'popular-shows', views.ShowsPopularViewSet,basename='popular-shows')
router.register(r'top-rated-shows', views.ShowsTopRatedViewSet,basename='top-rated-shows')
router.register(r'on-the-air-shows', views.ShowsOnTheAirViewSet,basename='upcoming-shows')
router.register(r'lastest-shows', views.ShowsLastestViewSet,basename='lastest-shows')
router.register(r'show', views.ShowViewSet,basename='show')
router.register(r'actors', views.ActorsViewSet,basename='actors')
router.register(r'actor', views.ActorViewSet,basename='actor')
router.register(r'credits', views.CreditsViewSet,basename='credits')

urlpatterns = [
    path('', include('management.urls')),
    path('social/', include('social_django.urls', namespace='social')),
    path('films/', include('movies.urls')),
    path('series/', include('shows.urls')),
    path('acteurs/', include('actors.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]