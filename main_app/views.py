from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



# ---------------- STATIC FILES
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# ---------------- ALBUMS
@login_required
def albums_index(request):
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            new_album = album_form.save(commit=False)
            new_album.user = request.user
            new_album.save()
            return redirect('albums_index')
    albums = Album.objects.all()
    album_form = AlbumForm()
    context = {
        'albums': albums,
        'album_form': album_form
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
            # return render(request, 'album/new.html', new_album.id)

            return redirect('album_details', new_album.id)
    else:
        form = AlbumForm()
        context = {'form': form}
        return render(request, 'albums/new.html', context)



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
def add_photo(request, album_id):
    album = Album.objects.get(id=album_id)
    return redirect('album_details', new_album.id)