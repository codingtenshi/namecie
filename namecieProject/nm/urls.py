
from django.urls import path, include
from nm.views import index, my_profile
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('my_profile/', views.my_profile, name='my_profile'),
]