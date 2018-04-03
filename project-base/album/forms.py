from django import forms
from .models import Album, Image, Comment, Like

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name',)

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('image',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)

class LikeForm(forms.ModelForm):

    class Meta:
        model = Like
        fields = ('like',)