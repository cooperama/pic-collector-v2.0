from django import forms
from .models import Album, Photo

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'use', 'description']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['url', 'photographer', 'photographer_url', 'src_medium']