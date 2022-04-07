from django.shortcuts import render
from django.views.generic import TemplateView

from ESGI_Movies.wrappe.tmdb import tmdb_tv

# Class Shows
# ===========
class ShowsView(TemplateView):
    def get(self,request,page=None,type=""):
        tv = tmdb_tv()

        if type=="": # Populaire
            shows = tv.popular(language='fr',page=page)
        elif type=="mieux-notées": # Mieux notées
            shows = tv.top_rated(language='fr',page=page)
        elif type=="en-cours-de-diffusion":
            shows = tv.on_the_air(language='fr',page=page)

        return render(request, 'pages/mediaview/medias.html', {'shows':shows['results'], 'total_pages':shows['total_pages'] })

class ShowDetailView(TemplateView):
    def get(self,request,tv_id):
        media = tmdb_tv(tv_id)
        response = media.detail(language='fr')
        
        credits = media.credits()
        videos = media.videos(language='fr')
        reviews = media.reviews(language='fr')

        return render(request, 'pages/mediaview/media.html', {'media':response, 'credits':credits['cast'][:8], 'videos':videos['results'][:4], 'reviews':reviews['results']})
# ===========