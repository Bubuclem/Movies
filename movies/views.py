from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

# Class Base
# ==========
class BaseView(TemplateView):
    def isNotauthenticated(self,request) -> bool :
        if request.user.is_authenticated:
            return True
        return False

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
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')
        return render(request, 'gallery/gallery.html', {})

    def post(self, request, id):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')
        return render(request, 'gallery/gallery.html', {'id':id})

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
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(request,username=_username,password=_password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'form/login.html', {})

class LogoutView(BaseView):
    def get(self,request):
        if self.isNotauthenticated(request) == False:
            return HttpResponseRedirect('/login')
        logout(request)
        return HttpResponseRedirect ('/login')