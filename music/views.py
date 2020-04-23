from django.shortcuts import render
from django.http import HttpResponse 
from django.urls import reverse 
from django.views import generic 


#import models 
from .models import *

# Create your views here.

def about(request):
    context = {
        'favorite_color': 'blue'
    }
    return render(request, 'music/about.html', context)

def index_view(request):
    ''' Return the last five musicians '''
    latest_musicians = Musician.objects.all() #Musician.objects.order_by('-pub_date')[:5]
    context = {'latest_musicians': latest_musicians}
    return render(request, 'music/index.html', context)

def musician_detail(request, musician_id):
    musician = Musician.objects.get(id=musician_id)
    everything = Album.objects.filter(artist=musician_id)
    context = {'musician': musician,
                'id': musician_id,
                'everything': everything,
                
            }
    return render(request, 'music/mdetails.html', context)

def album_detail(request, album_id):
    album_details = Album.objects.get(id=album_id)
    #pub_date = Album.objects.get(publish_date)
    context = {'album_details': album_details,
                'id': album_id}
    return render(request, 'music/adetails.html', context)

def song_detail(request, song_id):
    song_details = Song.objects.get(id=song_id)
    everything = Song.objects.all()
    context = {'song_details': song_details,
                'id':song_id}
    return render(request, 'music/sdetails.html', context)

def results_view(request, musician_id):
    musician_details = Musician.objects.get(id=musician_id)
    context = {'musician_details': musician_details,
                'id': musician_id}

    return render(request, 'music/results.html', context)
  
    
