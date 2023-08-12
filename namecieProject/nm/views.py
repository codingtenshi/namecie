from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .models import Profile
from django.contrib.auth.decorators import login_required

def index(request):
    is_registration = request.GET.get('registration')
    
    if is_registration == "true":
        profile = Profile()
        profile.save_user_info(request)
        user_info = Profile.objects.get(user_id=request.user)
        display_name = user_info.full_name
    else:
        try: 
            user_info = Profile.objects.get(user_id=request.user)
            display_name = user_info.display_name
        except:
            display_name = ''


    context = {
        'display_name': display_name,
    }

    return render(request, 'index.html', context)

@login_required # A user who is not logged in will be redirected to the login page before seeing his profile
def my_profile(request):
    user_info = Profile.objects.get(user_id=request.user)
    teams_admin = user_info.teams_admin.all();
    teams_admin_names = ', '.join([team.name for team in teams_admin])

    context = {
        'user': request.user,
        'first_name' : user_info.first_name,
        'last_name' : user_info.last_name,
        'full_name' : user_info.full_clean,
        'email' : user_info.email,
        'image' : user_info.image, 
        'display_name': user_info.display_name or '',
        'description': user_info.description,
        'teams_admin': teams_admin_names,
    }
    return render(request, 'my_profile.html', context)


def save(request):
    if request.method == 'POST':
        data = {
            'display_name': request.POST['display_name'],
            'description': request.POST['description'],
        }       
        profile = Profile.objects.get(user_id=request.user)
        profile.display_name = data['display_name']
        profile.description = data['description']
        profile.save()
        return redirect ('/')
    else:
        return render(request, 'my_profile.http')
