from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.views import View

from .forms import GenreForm, MovieForm, PersonForm, SearchForm
from .models import Genre, Job, Movie, MRating, Person, PersonMovie


def index(request):
    return render(request, "films/index.html")


class Movies(View):
    def get(self, request):
        movies = Movie.objects.all().order_by("-year")
        directors = Person.objects.filter(job=3)
        screenwriters = Person.objects.filter(job=2)
        message = request.GET.get("message", None)
        search_form = SearchForm()
        # below functionality of the search form
        title = request.GET.get("title")
        if title:
            movies = movies.filter(title__icontains=title)
        first_name = request.GET.get("first_name")
        if first_name:
            movies = (
                movies.filter(director__first_name=first_name)
                | movies.filter(screenplay__first_name=first_name)
                | movies.filter(starring__first_name=first_name)
            ).distinct()
        last_name = request.GET.get("last_name")
        if last_name:
            movies = (
                movies.filter(director__last_name=last_name)
                | movies.filter(screenplay__last_name=last_name)
                | movies.filter(starring__last_name=last_name)
            ).distinct()
        year = request.GET.get("year")
        if year:
            movies = movies.filter(year=year)

        movie_form = MovieForm()
        context = {
            "movies": movies,
            "directors": directors,
            "screenwriters": screenwriters,
            "message": message,
            "movie_form": movie_form,
            "search_form": search_form,
        }
        return render(request, "films/movies.html", context)

    def post(self, request):
        # breakpoint()
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            title = movie_form.cleaned_data["title"]
            new_movie = movie_form.save()
            return redirect(reverse("movies") + f"?message=Film {title} dodany do bazy")


class MovieDetails(View):
    def get(self, request, movie_id):
        movie = Movie.objects.get(pk=movie_id)
        people = Person.objects.all()
        genres = Genre.objects.all()
        rating_avg = 0
        ratings = movie.mrating_set.all()
        if ratings:
            rating_list = []
            for rating in ratings:
                rating_list.append(rating.rating)
            rating_avg = sum(rating_list) / len(rating_list)

        context = {
            "movie": movie,
            "people": people,
            "genres": genres,
            "ratings": ratings,
            "rating_avg": rating_avg,
        }
        return render(
            request,
            "films/movie.html",
            context,
        )


@login_required
def movie_comment_add(request, movie_id, person_id):
    if request.method == "POST":
        movie = Movie.objects.get(pk=movie_id)
        author = User.objects.get(pk=person_id)
        rating = request.POST["rating"]
        comment = request.POST["comment"]
        MRating.objects.create(
            movie=movie, rating=rating, comment=comment, author=author
        )
        return redirect(f"/movie-details/{movie_id}")


@login_required
def movie_person_add(request, movie_id):
    if request.method == "POST":
        movie = Movie.objects.get(pk=movie_id)
        person_id = request.POST["person_id"]
        person = Person.objects.get(pk=person_id)
        new_role = PersonMovie.objects.create(
            person=person, movie=movie, role=request.POST["role"]
        )
        return redirect(f"/movie-details/{movie_id}")


@login_required
def movie_person_remove(request, movie_id, person_id):
    person = Person.objects.get(pk=person_id)
    movie = Movie.objects.get(pk=movie_id)
    role_remove = PersonMovie.objects.filter(person=person, movie=movie)
    role_remove.delete()
    return redirect(f"/movie-details/{movie_id}")


@login_required
def movie_genre_add(request, movie_id):
    if request.method == "POST":
        movie = Movie.objects.get(pk=movie_id)
        genre_id = request.POST["genre_id"]
        genre = Genre.objects.get(pk=genre_id)
        add_genre = movie.genre.add(genre)
        return redirect(f"/movie-details/{movie_id}")


@login_required
def movie_genre_remove(request, movie_id, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    movie = Movie.objects.get(pk=movie_id)
    genre_remove = movie.genre.remove(genre)
    return redirect(f"/movie-details/{movie_id}")


class People(View):
    def get(self, request):
        persons = Person.objects.all()
        form = PersonForm()
        message = request.GET.get("message", None)
        return render(
            request,
            "films/persons.html",
            {"persons": persons, "form": form, "message": message},
        )

    def post(sef, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            message = f"Osoba {first_name} {last_name} dodana do bazy"
            form.save()
            return redirect(reverse("persons") + f"?message={message}")


class PersonDetails(View):
    def get(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = PersonForm(instance=person)
        message = request.GET.get("message", None)
        return render(request, "films/person.html", {"form": form, "message": message})

    def post(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = PersonForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            job = form.cleaned_data["job"]
            person.first_name = first_name
            person.last_name = last_name
            person.job = job
            person.save()
            return redirect(
                reverse("person", args=[person_id]) + "?message=Osoba zaktualizowana"
            )


@login_required
def delete_person(request, person_id):
    person = Person.objects.get(pk=person_id)
    message = f"Osoba {person.first_name} {person.last_name} usunięta"
    person.delete()
    return redirect(reverse("persons") + f"?message={message}")


class Genres(View):
    def get(self, request):
        if request.user.is_authenticated:
            genres = Genre.objects.all()
            message = None
            form = GenreForm()
            return render(
                request,
                "films/genres.html",
                {"genres": genres, "message": message, "form": form},
            )
        return redirect("/")

    def post(self, request):
        form = GenreForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            new_genres = form.save()
            return redirect(
                reverse("genres") + f"?message=Gatunek {name} dodady do bazy"
            )


@login_required
def delete_genre(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    genre.delete()
    return redirect("/genres/")
