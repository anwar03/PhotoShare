from django.db import models
from django.utils import timezone
from django.conf import settings


from album.models import Album


class Comment(models.Model):
    comment = models.CharField(max_length=255, blank=False)
    album = models.ForeignKey(Album, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=timezone.now())
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at', )
        verbose_name = ('Comment')
        verbose_name_plural = ('Comments')

    def __str__(self):
        return self.comment

