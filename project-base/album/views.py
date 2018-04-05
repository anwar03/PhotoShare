from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse_lazy

from .forms import AlbumForm
from .models import Album, Image, AlbumCollection
from comment.models import Comment
from like.models import Like


@method_decorator(login_required, name='dispatch')
class AlbumList(ListView):
    model = Album
    template_name = 'home.html'
    context_object_name = 'albums'
    
    def get_queryset(self):
        queryset = Album.objects.filter(publisher=self.request.user)
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

    def get_context_data(self, **kwargs):
        album = Album.objects.get(id=self.kwargs.get('pk'))
        self.comments = Comment.objects.filter(album_id=self.kwargs.get('pk'))
        likes = Like.objects.filter(album_id=self.kwargs.get('pk'))
        kwargs['album'] = album
        kwargs['comments']= self.comments
        kwargs['likes']= likes.count()
        kwargs['like'] = likes.last()

        return super().get_context_data(**kwargs)

    
    def get_queryset(self):
        queryset = AlbumCollection.objects.filter(album_id=self.kwargs.get('pk'))
        return queryset

