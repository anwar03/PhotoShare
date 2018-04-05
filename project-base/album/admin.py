from django.contrib import admin

from .models import Album, Image, AlbumCollection

admin.site.register(Album)
admin.site.register(Image)
admin.site.register(AlbumCollection)