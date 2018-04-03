from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import AlbumForm, CommentForm
from .models import Album, Image, Comment

@method_decorator(login_required, name='dispatch')
class AlbumList(ListView):
    model = Album
    template_name = 'home.html'
    context_object_name = 'albums'
    
    def get_queryset(self):
        self.album = Album.objects.filter(publisher=self.request.user)
        queryset = self.album
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



class CommentCreateView(CreateView):
    
    form_class = CommentForm
    template_name = 'comment.html'

    def get_context_data(self, **kwargs):
        self.album = Album.objects.get(id=self.kwargs.get('pk'))
        kwargs['album'] = self.album
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.pk = self.kwargs.get('pk')
        comment = form.save(commit=False)
        comment.album = Album.objects.get(id=self.kwargs.get('pk'))
        comment.save()
        return redirect('album-details', pk=self.pk)
   

class AlbumDetails(ListView):
    template_name = 'album-details.html'
    context_object_name = 'albums'

    def get_context_data(self, **kwargs):
        album = Album.objects.get(id=self.kwargs.get('pk'))
        kwargs['album'] = album
        self.comments = Comment.objects.filter(album_id=self.kwargs.get('pk'))
        kwargs['comments']= self.comments
        return super().get_context_data(**kwargs)

    
    def get_queryset(self):
        queryset = Album.objects.filter(id=self.kwargs.get('pk'))
        print('queryset: ', queryset)
        return queryset

