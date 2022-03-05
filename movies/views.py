from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Class Base
# ==========
class BaseView(TemplateView):
    def isNotauthenticated(self,request):
        if request.user.is_authenticated:
            return redirect('/login')

    def isStaff(self,request) -> bool:
        return request.user.is_staff

    def get(self,request):
        pass

    def post(self,request):
        pass

# Class Views
# ===========
class MediaView(BaseView):
    def get(self,request):
        self.isNotauthenticated()

class GenresView(BaseView):
    def get(self,request):
        self.isNotauthenticated()

class PoeplesView(BaseView):
    def get(self,request):
        self.isNotauthenticated()

class VideosView(BaseView):
    def get(self,request):
        self.isNotauthenticated()

class UtilisateursView(BaseView):
    def get(self,request):
        self.isNotauthenticated()
        if self.isStaff():
           pass

class LoginView(BaseView):
    def get(self,request):
        return render(request, 'form/login.html', {})

    def post(self,request):
        pass

class LogoutView(BaseView):
    def get(self,request):
        self.isNotauthenticated()