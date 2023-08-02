from django.shortcuts import render
from django.conf import settings
import requests

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





