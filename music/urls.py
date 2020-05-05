# music/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('musicians/', views.musicians, name='musicians'),
    path('musician/<int:musician_id>/', views.musician_info, name='musician_info'),
    path('album/<int:album_id>/', views.album_info, name='album_info'),
]