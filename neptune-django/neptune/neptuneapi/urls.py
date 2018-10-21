from django.urls import path

from neptuneapi.posts import views as post_routes
from neptuneapi.artists import views as artist_routes
from neptuneapi.albums import views as album_routes

"""neptune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin

urlpatterns = [
    path('posts/', post_routes.NeptunePostsRoute, name='NeptunePostsRoute'),
    path('artists', artist_routes.NeptuneArtistRoute, name='NeptuneArtistsRoute'),
    path('albums', album_routes.NeptuneAlbumRoute, name='NeptuneAlbumsRoute'),
]
