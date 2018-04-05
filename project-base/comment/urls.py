from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/comment/$', views.CommentCreateView.as_view(), name='comment'),
    url(r'^(?P<comment_pk>\d+)/delete/$', views.CommentDeleteView.as_view(), name='comment-delete'),
]
