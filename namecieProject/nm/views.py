from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .models import Profile
from django.contrib.auth.decorators import login_required
from .modules.profile import get_user_info

def index(request):
    user_info = get_user_info(request.user)

    context = {
        'display_name': user_info['display_name'],
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
    
    user_info = get_user_info(request.user)
    
    context = {
        'user': request.user,
        'first_name' : traits.get('first_name', None),
        'last_name' : traits.get('last_name', None),
        'email' : traits.get('email', None),
        'picture' : traits.get('picture', None), 
        'display_name': user_info['display_name'],
        'description': user_info['description']  
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





