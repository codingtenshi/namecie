from django.urls import path
from account.views import AccountIndexView


urlpatterns = [
    path('', AccountIndexView.as_view(), name='index'),
]
