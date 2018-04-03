from django.contrib import admin

from .models import Album, Image, Comment

admin.site.register(Album)
admin.site.register(Image)
admin.site.register(Comment)
