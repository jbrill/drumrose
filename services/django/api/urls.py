"""
Urls Module
"""

from django.contrib import admin
from django.urls import path

from api.posts import views as post_routes
from api.artists import views as artist_routes
from api.albums import views as album_routes
from api.songs import views as song_routes
from api.users import views as user_routes
from api.auth import views as auth_routes

""" URL Configuration

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

urlpatterns = [
    path(
        'auth/',
        auth_routes.AuthRoute.as_view(),
        name='Auth'
    ),
    path(
        'posts/',
        post_routes.PostList.as_view(),
        name='PostsList'
    ),
    path(
        'posts/<post_id>/',
        post_routes.PostDetail.as_view(),
        name='PostsDetail'
    ),
    path(
        'songs/',
        song_routes.SongList.as_view(),
        name='SongList'
    ),
    path(
        'songs/<song_id>/',
        song_routes.SongDetail.as_view(),
        name='SongDetail'),
    path(
        'artists',
        artist_routes.ArtistRoute,
        name='ArtistsRoute'
    ),
    path(
        'albums',
        album_routes.AlbumRoute,
        name='AlbumsRoute'
    ),
    path(
        'users/',
        user_routes.UserList.as_view(),
        name='UserList'
    ),
    path(
        'users/<user_handle>/',
        user_routes.UserDetail.as_view(),
        name='UserDetail'
    ),
]
