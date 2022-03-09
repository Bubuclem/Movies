from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from movies import views

#router = routers.DefaultRouter()
#router.register(r'api-movies', views.API_Movies)

urlpatterns = [
    path('', include('movies.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]