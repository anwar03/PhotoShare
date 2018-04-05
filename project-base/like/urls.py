from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/like/$', views.LikeCreate.as_view(), name='like'),
    url(r'^(?P<like_pk>\d+)/dislike/$', views.DisLike.as_view(), name='dislike'),

]
