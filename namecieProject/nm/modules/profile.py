from nm.models import Profile
from django.conf import settings
import requests



def get_user_info(user):
    try:
        profile = Profile.objects.get(user_id=user)
        first_name = profile.first_name
        last_name = profile.last_name or "Brak nazwiska"
        full_name = profile.full_name or "Brak imienia i nazwiska"
        image = profile.image
        email = profile.email or "Brak adresu email"
        display_name = profile.display_name
        description = profile.description
    except Profile.DoesNotExist:
        display_name = "Nie znaleziono profilu"
        description = "Nie znaleziono opisu"
        first_name = "Brak imienia"
        last_name = full_name = image = email = ""
    
    return {
        'first_name': first_name,
        'last_name': last_name,
        'full_name': full_name,
        'image': image,
        'email': email,
        'display_name': display_name,
        'description': description
        }


def save_user_info(request):
    sdk_url = settings.ORY_SDK_URL
    sess = requests.get(
            f"{sdk_url}/sessions/whoami",
            cookies=request.COOKIES
        )
    
    traits = sess.json().get('identity', {}).get('traits', None) # dict
    full_name = traits.get('first_name') + " " + traits.get('last_name') # str

    profile = Profile()
    profile.first_name = traits.get('first_name', None)
    profile.last_name  = traits.get('last_name', None)
    profile.full_name = full_name
    profile.image = traits.get('picture', None)
    profile.email = traits.get('email', None)
    profile.user_id = request.user
    profile.save()


    