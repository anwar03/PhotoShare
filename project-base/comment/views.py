from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse_lazy

from .forms import CommentForm
from .models import Comment
from album.models import Album


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
        comment.album = Album.objects.get(id=self.pk)
        comment.save()
        return redirect('album-details', pk=self.pk)


