"""
Urls Module
"""

from api import views as api_routes
from api.albums import views as album_routes
from api.apple_music_token import views as apple_music_token_routes
from api.artists import views as artist_routes
from api.auth import views as auth_routes
from api.posts import views as post_routes
from api.songs import views as song_routes
from api.users import views as user_routes
from django.urls import path


urlpatterns = [
    path("", api_routes.HealthRoute.as_view(), name="Health"),
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
    path("artists/", artist_routes.ArtistRoute.as_view(), name="ArtistsRoute"),
    path("albums/", album_routes.AlbumRoute.as_view(), name="AlbumsRoute"),
    path("users/", user_routes.UserList.as_view(), name="UserList"),
    path(
        "users/<user_handle>/",
        user_routes.UserDetail.as_view(),
        name="UserDetail",
    ),
    path(
        "apple_music_token/",
        apple_music_token_routes.AppleMusicTokenRoute.as_view(),
        name="AppleMusicTokenRoute",
    ),
]
