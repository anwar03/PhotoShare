from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import AlbumForm
from .models import Album, Image, Comment, AlbumCollection


@method_decorator(login_required, name='dispatch')
class AlbumList(ListView):
    model = Album
    template_name = 'home.html'
    context_object_name = 'albums'
    
    def get_queryset(self):
        self.album = Album.objects.filter(publisher=self.request.user)
        queryset = self.album
        print('queryset: ', queryset)
        print('HOST: ', settings.ALLOWED_HOSTS)
        return queryset


@method_decorator(login_required, name='dispatch')
class CreateAlbum(CreateView):
    form_class = AlbumForm
    template_name = 'album.html'

    def form_valid(self, form):
        album = form.save(commit=False)
        album.publisher = self.request.user
        album.save()
        return redirect('home')

class AlbumDetails(ListView):
    template_name = 'album-details.html'
    context_object_name = 'albums'
    
    def get_queryset(self):
        queryset = Album.objects.filter(publisher=self.request.user)
        return queryset

