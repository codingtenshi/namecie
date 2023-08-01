from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def my_profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'my_profile.html', context)





