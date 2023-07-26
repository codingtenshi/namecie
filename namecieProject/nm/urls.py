
from django.urls import path, include
from nm.views import index, login
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('login/', views.login, name='login'),
]