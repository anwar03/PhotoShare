from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .forms import LikeForm
from .models import  Like
from album.models import Album



class Like(CreateView):
    
    form_class = LikeForm
    template_name = 'like.html'

    def get_context_data(self, **kwargs):
        self.album = Album.objects.get(id=self.kwargs.get('pk'))
        kwargs['album'] = self.album
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.pk = self.kwargs.get('pk')
        like = form.save(commit=False)
        like.album = Album.objects.get(id=self.kwargs.get('pk'))
        like.save()
        return redirect('album-details', pk=self.pk)


class DisLike(DeleteView):
    model = Like
    template_name = 'like_confirm_delete.html'
    pk_url_kwarg = 'like_pk'
    
    def get_success_url(self):
        self.like = Like.objects.get(id=self.kwargs.get('like_pk'))
        return reverse_lazy('album-details', kwargs={'pk': self.like.album.id})
