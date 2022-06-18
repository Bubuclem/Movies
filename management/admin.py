from django.contrib import admin

from .models import Watched, Review, Credit, Cast, Crew, SpokenLanguage

class SpokenLanguageAdmin(admin.ModelAdmin):
    list_display = ('iso_639_1', 'name')

admin.site.register(SpokenLanguage,SpokenLanguageAdmin)

class WatchedAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'media_id', 'media_type', 'pub_date')

admin.site.register(Watched,WatchedAdmin)

admin.site.register(Review)

admin.site.register(Cast)
admin.site.register(Crew)

class CreditAdmin(admin.ModelAdmin):
    list_display = ('media_type', )
    list_filter = ('media_type',)

admin.site.register(Credit, CreditAdmin)