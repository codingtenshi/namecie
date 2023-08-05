
from django.urls import path, include
from nm.views import index, my_profile
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('save_form_data/', views.save, name='save_form_data'),
]