from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('albums/', views.albums_index, name='albums_index'),
    path('albums/add_album', views.add_album, name='add_album'),
    path('albums/<int:album_id>/', views.album_details, name='album_details'),
    path('albums/<int:album_id>/add_photo', views.add_photo, name='add_photo'),
]