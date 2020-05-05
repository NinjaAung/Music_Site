# music/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician


def home(request):
    return HttpResponse("Music_Site")

def musicians(request):
    context = {
        'musicians': Musician.objects.all()
    }
    return render(request, 'musicians.html', context)


def musician_info(request, musician_id):
    context = {
        'musician': Musician.objects.get(id=musician_id),
        'albums': Album.objects.filter(artist=musician_id)

    }
    return render(request, 'musician_info.html', context)


def album_info(request, album_id):
    context = {
        'album': Album.objects.get(id=album_id),
        'songs': Song.objects.filter(album=album_id)

    }
    return render(request, 'album_info.html', context)