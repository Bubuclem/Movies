from django.contrib import admin
from .models import Actor

class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'popularity')
    search_fields = ('id', 'name')

admin.site.register(Actor, ActorAdmin)