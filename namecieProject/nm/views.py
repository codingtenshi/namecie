from django.shortcuts import render, redirect
from django.conf import settings
import requests

from .models import Profile
from django.contrib.auth.decorators import login_required

def index(request):
    try:
        profile = Profile.objects.get(user_id=request.user)
        display_name = profile.display_name
    except Profile.DoesNotExist:
        display_name = "Nie znaleziono profilu"

    context = {
        'display_name': display_name,
    }

    return render(request, 'index.html', context)

@login_required # A user who is not logged in will be redirected to the login page before seeing his profile
def my_profile(request):
    sdk_url = settings.ORY_SDK_URL
    sess = requests.get(
            f"{sdk_url}/sessions/whoami",
            cookies=request.COOKIES
        )
    traits = sess.json().get('identity', {}).get('traits', None)

    try:
        profile = Profile.objects.get(user_id=request.user)
        display_name = profile.display_name
        description = profile.description
    except Profile.DoesNotExist:
        display_name = "Nie znaleziono profilu"
        description = "Nie znaleziono opisu"
    
        
    context = {
        'user': request.user,
        'first_name' : traits.get('first_name', None),
        'last_name' : traits.get('last_name', None),
        'email' : traits.get('email', None),
        'picture' : traits.get('picture', None), 
        'display_name': display_name,
        'description': description  
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
        profile.user_id = request.user
        profile.save()
        return redirect ('/')
    else:
        return render(request, 'my_profile.http')





