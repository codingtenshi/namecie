from django.shortcuts import render


def strona_startowa(request):
    return render(request, 'namecie.pl.html')

def zaloguj(request):
    return render(request, 'zaloguj.html')

