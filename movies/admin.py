from django.contrib import admin

from .models import Movie, Genre

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','release_date', 'vote_average', 'vote_count','popularity')
    search_fields = ('title',)

admin.site.register(Movie,MovieAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

admin.site.register(Genre,GenreAdmin)