from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class AccountIndexView(TemplateView):
    """
        renders the index.html for the root '/'
    """
    template_name = 'index.html'


class AccountLoginView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('account:index')
    next_page = reverse_lazy('account:index')

