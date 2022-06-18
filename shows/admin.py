from django.contrib import admin

from .models import Show, Genre

class ShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'status','first_air_date', 'vote_average', 'vote_count', 'popularity')
    search_fields = ('name',)
    exclude = ('last_episode', 'seasons')
    
admin.site.register(Show,ShowAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

admin.site.register(Genre,GenreAdmin)