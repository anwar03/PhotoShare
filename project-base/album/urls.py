from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^add/$', views.CreateAlbum.as_view(), name='album'),
    url(r'^(?P<slug>[\w\-]{10})/$', views.AlbumDetails.as_view(), name='album-details'),

]
