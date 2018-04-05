from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.conf import settings
from django.urls import reverse_lazy

from .forms import CommentForm
from .models import Comment
from album.models import Album


class CommentCreateView(CreateView):
    """ Create Comment view for viewer and return album details."""

    form_class = CommentForm
    template_name = 'comment.html'

    def get_context_data(self, **kwargs):
        self.album = Album.objects.get(id=self.kwargs.get('pk'))
        kwargs['album'] = self.album
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.pk = self.kwargs.get('pk')
        comment = form.save(commit=False)
        comment.album = Album.objects.get(id=self.pk)
        comment.save()
        return redirect('album-details', pk=self.pk)


class CommentUpdateView(UpdateView):
    """Comment Update view for owner. but this field is not used because of all viewer not register user."""

    form_class = CommentForm
    template_name = 'edit_comment.html'
    pk_url_kwarg = 'comment_pk'
    context_object_name = 'comment'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs.get('comment_pk'))

    def form_valid(self, form):
        comment = form.save(commit=False)
        self.album = Album.objects.get(id=self.kwargs.pk)
        comment.save()
        return redirect('album-details', pk=self.album.pk)



class CommentDeleteView(DeleteView):
    """ Delete view only for album Publisher."""
    model = Comment
    template_name = 'comment_confirm_delete.html'
    pk_url_kwarg = 'comment_pk'
    
    def get_success_url(self, **kwargs):
        self.comment = Comment.objects.get(id=self.kwargs.get('comment_pk'))
        kwargs['comment'] = self.comment
        return reverse_lazy('album-details', kwargs={'pk': self.comment.album.id})
