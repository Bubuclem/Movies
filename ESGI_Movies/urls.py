from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from movies import views
from shows import views
from actors import views

router = routers.DefaultRouter()
# router.register(r'api-series', views.ShowsViewSet)

urlpatterns = [
    path('', include('movies.urls')),
    path('séries', include('shows.urls')),
    path('acteurs', include('actors.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]