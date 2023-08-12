from django.shortcuts import render

def create_team(request):
    return render(request, 'create_team.html')
