from django.contrib import admin

from .models import Album, Image, Like, Comment, AlbumCollection

admin.site.register(Album)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(AlbumCollection)