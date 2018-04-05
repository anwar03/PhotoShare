import string as str
import uuid
from random import choice

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.db.models import permalink



def get_image_filename(instance, filename):
    return "album/%s/%s" % (instance.name, filename)

def slug_generator():
        n = 10
        random = str.ascii_uppercase + str.ascii_lowercase + str.digits
        return ''.join(choice(random) for _ in range(n))

def password_generator():
        n = 6
        random = str.ascii_uppercase + str.ascii_lowercase + str.digits
        return ''.join(choice(random) for _ in range(n))


class Album(models.Model):
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='album', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(default=slug_generator, unique=True, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(default=password_generator, unique=True, max_length=6)
    

    def __str__(self):
        return self.name

    def get_absulate_url(self):
        url = reverse('album-details', kwargs={ 'pk': self.id } )
        return "%s%s" % ('http://localhost:8000', url)

    


class Image(models.Model):
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=get_image_filename)

    def __str__(self):
        return self.name

    

class AlbumCollection(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{}'.format(self.album.name)

    class Meta:
        unique_together = ('album', 'image')
        index_together = ('album', 'image')

