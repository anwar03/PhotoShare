from django.db import models
from django.utils import timezone
from django.urls import reverse


from album.models import Album


class Like(models.Model):
    album = models.ForeignKey(Album, related_name='likes', on_delete=models.CASCADE)
    like = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

