from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import requests, random



# ---------------- STATIC FILES
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# ---------------- ALBUMS
@login_required
def albums_index(request):
    albums = Album.objects.all()
    context = {
        'albums': albums
    }
    return render(request, 'album/index.html', context)


@login_required
def add_album(request):
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            new_album = album_form.save(commit=False)
            new_album.user = request.user
            new_album.save()
            # Need to get photos now... I guess can always add/delete photos from album details page.
            # Render add_photoss page...?

            return redirect('album_details', new_album.id)
    else:
        form = AlbumForm()
        context = {'form': form}
        return render(request, 'album/new.html', context)



@login_required
def album_details(request, album_id):
    album = Album.objects.get(id=album_id)
    form = PhotoForm()
    context = {
        'album': album,
        'form': form 
    }
    return render(request, 'album/details.html', context)


# ---------------- PHOTOS
@login_required
def add_photos(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        photo_form = PhotoForm(request.POST)
        if photo_form.is_valid():
            # I don't think it needs to be associated with the user. Just the album.
            # new_photo = photo_form.save(commit=False)
            # new_photo.user = request.user
            new_photo.save()
            return redirect('album_details', new_album.id)
    else:
        headers = {'Authorization': '563492ad6f917000010000018e29e5d933e64dc19b96c9ddd87d413f'}
        params = {'per_page': '80', 'query': 'animal', 'query': 'happy'}
        
        r = requests.get('https://api.pexels.com/v1/search', headers=headers, params=params)

        # r = requests.get(f'https://api.pexels.com/v1/curated', headers=headers, params=params)
        photos = r.json()['photos']
        random.shuffle(photos)
        context = {
            'album': album,
            'photos': photos[:10]
        }
        return render(request, 'photos/new.html', context)

