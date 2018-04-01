from django.db import models
from django.utils import timezone
from django.conf import settings

def get_image_filename(instance, filename):
    album_name = instance.album_name
    return "album/%s/%s" % (album_name, filename)



class Image(models.Model):
    image = models.ImageField(upload_to=get_image_filename)

class Album(models.Model):
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='album', on_delete=models.CASCADE)
    album_name = models.CharField(max_length=31, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=timezone.now)
    image = models.ImageField(upload_to=get_image_filename)
    #url = models.URLField(max_length=255, default=get_absulate_url)
    #password = models.CharField()


    def __str__(self):
        return self.album_name

