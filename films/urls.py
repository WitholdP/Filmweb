from django.urls import path

from films.views import (
    Genres,
    MovieDetails,
    Movies,
    People,
    PersonDetails,
    delete_genre,
    delete_person,
    index,
    movie_comment_add,
    movie_genre_add,
    movie_genre_remove,
    movie_person_add,
    movie_person_remove,
)

urlpatterns = [
    path("", index, name="index"),
    path("movies/", Movies.as_view(), name="movies"),
    path("movie-details/<int:movie_id>/", MovieDetails.as_view(), name="movie"),
    path(
        "movie-comment-add/<int:movie_id>/<int:person_id>",
        movie_comment_add,
        name="movie_comment_add",
    ),
    path("movie-genre-add/<int:movie_id>", movie_genre_add, name="movie_genre_add"),
    path(
        "movie-genre-remove/<int:movie_id>/<int:genre_id>",
        movie_genre_remove,
        name="movie_genre_remove",
    ),
    path("movie-person-add/<int:movie_id>", movie_person_add, name="movie_person_add"),
    path(
        "movie-person-remove/<int:movie_id>/<int:person_id>/",
        movie_person_remove,
        name="movie_person_remove",
    ),
    path("persons/", People.as_view(), name="persons"),
    path("person/<int:person_id>/", PersonDetails.as_view(), name="person"),
    path("delete-person/<int:person_id>/", delete_person, name="delete_person"),
    path("genres/", Genres.as_view(), name="genres"),
    path("delete-genre/<int:genre_id>/", delete_genre, name="delete_genre"),
]
