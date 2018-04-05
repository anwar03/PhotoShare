from django import forms
from .models import Album, Image

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name',)

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('image',)

