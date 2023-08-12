from django.urls import path
from . import views

urlpatterns = [
    path('create_team/', views.create_team, name='create_team'),
    path('save_team/', views.save_team, name='save_team'),
]