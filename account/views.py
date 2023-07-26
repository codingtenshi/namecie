from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class AccountIndexView(TemplateView):
    """
        renders the index.html for the root '/'
    """
    template_name = 'index.html'


class AccountLoginView(LoginView):
    """
        login user nad return to index
    """
    template_name = 'account/login.html'
    success_url = reverse_lazy('account:index')
    next_page = reverse_lazy('account:index')


class AccountLogoutView(LogoutView):
    """
    Log out the user and redirect to login Page.
    """
    next_page = reverse_lazy("account:login")
