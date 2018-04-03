from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^add/$', views.CreateAlbum.as_view(), name='album'),
    url(r'^(?P<pk>\d+)/$', views.AlbumDetails.as_view(), name='album-details'),
    url(r'^(?P<pk>\d+)/like/$', views.LikeCreate.as_view(), name='like'),
    url(r'^(?P<like_pk>\d+)/dislike/$', views.DisLike.as_view(), name='dislike'),
    url(r'^(?P<pk>\d+)/comment/$', views.CommentCreateView.as_view(), name='comment'),

]
