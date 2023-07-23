from django.views.generic import TemplateView


class AccountIndexView(TemplateView):
    """
        renders the index.html for the root '/'
    """
    template_name = 'account/index.html'
