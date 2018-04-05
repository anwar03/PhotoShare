from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/comment/$', views.CommentCreateView.as_view(), name='comment'),

]
