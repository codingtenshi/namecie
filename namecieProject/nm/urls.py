
from django.urls import path, include
from nm.views import strona_startowa, zaloguj
from . import views

urlpatterns = [
    path('', strona_startowa, name='strona_startowa'),
    path('zaloguj/', views.zaloguj, name='zaloguj'),
]