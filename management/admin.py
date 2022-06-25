from django.contrib import admin

from .models import Watched, Favorite,Review, SpokenLanguage

class SpokenLanguageAdmin(admin.ModelAdmin):
    list_display = ('iso_639_1', 'name')

admin.site.register(SpokenLanguage,SpokenLanguageAdmin)

class WatchedAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'media_id', 'media_type', 'pub_date')

admin.site.register(Watched,WatchedAdmin)

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'media_id', 'media_type', 'pub_date')

admin.site.register(Favorite,FavoriteAdmin)

admin.site.register(Review)