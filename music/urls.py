from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.index_view, name='index'),
    path('about-me/', views.about, name='about'),
    path('<int:musician_id>/musician/', views.musician_detail, name='mdetails'),
    path('<int:album_id>/album/', views.album_detail, name='adetails'),
    path('<int:song_id>/song/', views.song_detail, name='sdetails'),
    path('<int:musician_id/results/', views.results_view, name='results'),

    

]
