from django.contrib import admin

from .models import Watched, Review, Credit, Cast, Crew

admin.site.register(Watched)

admin.site.register(Review)

admin.site.register(Cast)
admin.site.register(Crew)

class CreditAdmin(admin.ModelAdmin):
    list_display = ('media_type', )
    list_filter = ('media_type',)

admin.site.register(Credit, CreditAdmin)