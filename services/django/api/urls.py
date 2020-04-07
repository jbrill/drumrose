"""
Urls Module
"""

from api.albums import views as album_routes
from api.artists import views as artist_routes
from api.auth import views as auth_routes
from api.posts import views as post_routes
from api.songs import views as song_routes
from api.users import views as user_routes
from django.urls import path

urlpatterns = [
    path("auth/", auth_routes.AuthRoute.as_view(), name="Auth"),
    path("posts/", post_routes.PostList.as_view(), name="PostsList"),
    path(
        "posts/<post_id>/",
        post_routes.PostDetail.as_view(),
        name="PostsDetail",
    ),
    path("songs/", song_routes.SongList.as_view(), name="SongList"),
    path(
        "songs/<song_id>/", song_routes.SongDetail.as_view(), name="SongDetail"
    ),
    path("artists", artist_routes.ArtistRoute, name="ArtistsRoute"),
    path("albums", album_routes.AlbumRoute, name="AlbumsRoute"),
    path("users/", user_routes.UserList.as_view(), name="UserList"),
    path(
        "users/<user_handle>/",
        user_routes.UserDetail.as_view(),
        name="UserDetail",
    ),
]
