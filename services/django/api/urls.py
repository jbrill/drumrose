"""
Urls Module
"""
from api import views as api_routes
from api.albums import views as album_routes
from api.apple_music_token import views as apple_music_token_routes
from api.artists import views as artist_routes
from api.favorites import views as favorite_routes
from api.playlists import views as playlist_routes
from api.reviews import views as review_routes
from api.songs import views as song_routes
from api.users import views as user_routes
from django.urls import path

urlpatterns = [
    path("", api_routes.HealthRoute.as_view(), name="HealthCheck"),
    path(
        "reviews/tracks/",
        review_routes.TrackReviewList.as_view(),
        name="TrackReviewList",
    ),
    path(
        "reviews/albums/",
        review_routes.AlbumReviewList.as_view(),
        name="AlbumReviewList",
    ),
    path(
        "reviews/playlists/",
        review_routes.PlaylistReviewList.as_view(),
        name="PlaylistReviewList",
    ),
    path(
        "<user_id>/favorites/",
        user_routes.UserFavoritesList.as_view(),
        name="UserFavoritesList",
    ),
    path(
        "favorites/tracks/",
        favorite_routes.FavoriteTracksList.as_view(),
        name="FavoriteTracksList",
    ),
    path(
        "favorites/albums/",
        favorite_routes.FavoriteAlbumList.as_view(),
        name="FavoriteAlbumsList",
    ),
    path(
        "favorites/playlists/",
        favorite_routes.FavoritePlaylistList.as_view(),
        name="FavoritePlaylistsList",
    ),
    path("playlists/", playlist_routes.PlaylistList.as_view(), name="PlaylistList"),
    path(
        "playlists/<playlist_id>/",
        playlist_routes.PlaylistDetail.as_view(),
        name="PlaylistDetail",
    ),
    path("tracks/", song_routes.SongList.as_view(), name="SongList"),
    path("tracks/<track_id>/", song_routes.SongDetail.as_view(), name="SongDetail"),
    path("artists/", artist_routes.ArtistRoute.as_view(), name="ArtistsRoute"),
    path("albums/", album_routes.AlbumRoute.as_view(), name="AlbumsRoute"),
    path("albums/<album_id>/", album_routes.AlbumDetail.as_view(), name="AlbumDetail"),
    path("users/", user_routes.UserList.as_view(), name="UserList"),
    path("users/<user_handle>/", user_routes.UserDetail.as_view(), name="UserDetail"),
    path(
        "apple_music_token/",
        apple_music_token_routes.AppleMusicTokenRoute.as_view(),
        name="AppleMusicTokenRoute",
    ),
]
