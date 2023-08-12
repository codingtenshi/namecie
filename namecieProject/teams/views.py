from django.shortcuts import render, redirect
from.forms import TeamForm
from .models import Team
from nm.models import Profile

def create_team(request):
    form = TeamForm()
    return render(request, 'create_team.html', {'form': form})

def save_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
           admin = Profile.objects.get(user_id=request.user)
           team = Team()
           team.name=form.cleaned_data['name']
           team.team_description=form.cleaned_data['team_description']
           team.year_founded=form.cleaned_data['year_founded']
           team.save()
           team.admins.add(admin)

        return redirect('/')