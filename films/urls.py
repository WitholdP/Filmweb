from django.urls import path

from films.views import (
    delete_genre,
    delete_person,
    genres,
    index,
    movie,
    movie_genre_add,
    movie_genre_remove,
    movie_person_add,
    movie_person_remove,
    movies,
    person,
    persons,
)

urlpatterns = [
    path("", index, name="index"),
    path("movies/", movies, name="movies"),
    path("movie-details/<int:movie_id>/", movie, name="movie"),
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
    path("persons/", persons, name="persons"),
    path("edit-person/<int:person_id>/", person, name="person"),
    path("delete-person/<int:person_id>/", delete_person, name="delete_person"),
    path("genres/", genres, name="genres"),
    path("delete-genre/<int:genre_id>/", delete_genre, name="delete_genre"),
]
