from django.urls import path
from account.views import AccountIndexView, AccountLoginView

app_name = 'account'

urlpatterns = [
    path('', AccountIndexView.as_view(), name='index'),

    # auth
    path('login/', AccountLoginView.as_view(), name='login'),
]
