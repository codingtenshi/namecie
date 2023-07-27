
from django.urls import path, include
from nm.views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
]