import string as str
from random import choice

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.db.models import permalink



def get_image_filename(instance, filename):
    name = instance.name
    return "album/%s/%s" % (name, filename)

def slug_generator():
        n = 10
        random = str.ascii_uppercase + str.ascii_lowercase + str.digits
        return ''.join(choice(random) for _ in range(n))

def password_generator():
        n = 6
        random = str.ascii_uppercase + str.ascii_lowercase + str.digits
        return ''.join(choice(random) for _ in range(n))

class Image(models.Model):
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images', on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=get_image_filename)



class Album(models.Model):
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='album', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(default=slug_generator, unique=True, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(default=password_generator, unique=True, max_length=6)


    def __str__(self):
        return self.name

    
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
        truncated_comment = Truncator(self.comment)
        return truncated_comment.chars(100)
    

class AlbumCollection(models.Model):
    album = models.ForeignKey(Album, related_name='comments', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='comments', on_delete=models.CASCADE) 