from django.conf.urls import url, include


from . import views
from like.views import Like, DisLike

urlpatterns = [
    url(r'^add/$', views.CreateAlbumView.as_view(), name='album'),
    url(r'^(?P<pk>\d+)/$', views.AlbumDetailsView.as_view(), name='album-details'),
    url(r'^', include('like.urls')),
    url(r'^', include('comment.urls')),
    
    
]
