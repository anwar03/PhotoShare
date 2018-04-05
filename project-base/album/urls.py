from django.conf.urls import url, include


from . import views
from like.views import Like, DisLike

urlpatterns = [
    url(r'^add/$', views.CreateAlbum.as_view(), name='album'),
    url(r'^(?P<pk>\d+)/$', views.AlbumDetails.as_view(), name='album-details'),
    url(r'^(?P<pk>\d+)/like/$', Like.as_view(), name='like'),
    url(r'^(?P<like_pk>\d+)/dislike/$', DisLike.as_view(), name='dislike'),
    url(r'^', include('comment.urls')),
    
    
]
