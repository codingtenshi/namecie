from nm.models import Profile
from requests import request


def get_user_info(user):
    try:
        profile = Profile.objects.get(user_id=user)
        display_name = profile.display_name
        description = profile.description
    except Profile.DoesNotExist:
        display_name = "Nie znaleziono profilu"
        description = "Nie znaleziono opisu"
    
    return {'display_name': display_name , 'description': description}


#def save_user_info