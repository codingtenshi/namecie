from django.shortcuts import render, redirect
from django.conf import settings
import requests
from django.urls import reverse
from django.http import HttpResponse
from .models import Profile

def index(request):
    return render(request, 'index.html')


def my_profile(request):
    sdk_url = settings.ORY_SDK_URL
    sess = requests.get(
            f"{sdk_url}/sessions/whoami",
            cookies=request.COOKIES
        )
    traits = sess.json().get('identity', {}).get('traits', None)
    
        
    context = {
        'user': request.user,
        'first_name' : traits.get('first_name', None),
        'last_name' : traits.get('last_name', None),
        'email' : traits.get('email', None),
        'picture' : traits.get('picture', None),   
    }
    return render(request, 'my_profile.html', context)
 

def save(request):
    if request.method == 'POST':
        data = {
            'display_name': request.POST['display_name'],
            'description': request.POST['description'],
        }       
        profile = Profile()
        profile.display_name = data['display_name']
        profile.description = data['description']
        profile.save()
        return redirect ('/')
    else:
        return render(request, 'my_profile.http')





