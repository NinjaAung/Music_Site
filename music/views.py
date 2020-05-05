from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician


def home(request):
    return HttpResponse("Music_Site")
