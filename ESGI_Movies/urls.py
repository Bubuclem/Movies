from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'movies', views.MovieViewSet)

urlpatterns = [
    path('', include('management.urls')),
    path('films/', include('movies.urls')),
    path('series/', include('shows.urls')),
    path('acteurs/', include('actors.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]