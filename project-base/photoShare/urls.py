from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from publisher import views

urlpatterns =[

    path(r'admin/', admin.site.urls),
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^publisher/', include('publisher.urls')),
    url(r'^album/', include('album.urls')),
]
