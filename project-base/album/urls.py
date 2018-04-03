from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^add/$', views.CreateAlbum.as_view(), name='album'),
    url(r'^(?P<pk>\d+)/$', views.AlbumDetails.as_view(), name='album-details'),
    url(r'^(?P<pk>\d+)/comment/$', views.CommentCreateView.as_view(), name='comment'),

]
