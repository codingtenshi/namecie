
from django.urls import path, include
from nm.views import strona_startowa

urlpatterns = [
    path('', strona_startowa),
]