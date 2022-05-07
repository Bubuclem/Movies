from django.views.generic import TemplateView

TEMPLATE_BASE = 'pages/management/'

# Class de connexion
# ===========
class LoginView(TemplateView):

    template_name = TEMPLATE_BASE + 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self,request):
        pass

# Class de déconnexion
# ===========
class LogoutView(TemplateView):

    template_name = TEMPLATE_BASE + 'logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context