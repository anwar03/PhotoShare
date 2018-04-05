from django.conf.urls import url, include


from . import views

urlpatterns = [
    url(r'^add/$', views.CreateAlbum.as_view(), name='album'),
    url(r'^(?P<pk>\d+)/$', views.AlbumDetails.as_view(), name='album-details'),
    url(r'', include('comment.urls')),
    url(r'', include('like.urls')),
    
]
