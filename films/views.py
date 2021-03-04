from django.shortcuts import render, redirect
from .models import Movie, Person, Genre, PersonMovie, Job


def index(request):
    return render(request, 'index.html')

def movies(request):
    movies = Movie.objects.all().order_by('-year')
    directors = Person.objects.filter(job = 3)
    screenwriters = Person.objects.filter(job = 2)
    message = None
    context = {
    'movies': movies,
    'directors': directors,
    'screenwriters': screenwriters,
    'message': message
    }
    if request.method == 'POST':
        title = request.POST['title']
        year = request.POST['year']
        rating = request.POST['rating']
        director_id = request.POST['director_id']
        screenplay_id = request.POST['screenplay_id']
        new_movie = Movie.objects.create(title = title, year = year, rating = rating, director_id = director_id, screenplay_id = screenplay_id)
        context['message'] = f"Film {title} dodany do bazy"
    return render(request, 'movies.html', context)

def movie(request, movie_id):
    movie = Movie.objects.get(pk = movie_id)
    people = Person.objects.all()
    genres = Genre.objects.all()
    return render(request, 'movie.html', {'movie': movie, 'people': people, 'genres': genres})

def movie_person_add(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk = movie_id)
        person_id = request.POST['person_id']
        person = Person.objects.get(pk = person_id)
        new_role = PersonMovie.objects.create(person = person, movie = movie, role = request.POST['role'])
        return redirect(f'/movie-details/{movie_id}')

def movie_person_remove(request, movie_id, person_id):
    person = Person.objects.get(pk = person_id)
    movie = Movie.objects.get(pk = movie_id)
    role_remove = PersonMovie.objects.filter(person = person, movie = movie)
    role_remove.delete()
    return redirect(f'/movie-details/{movie_id}')

def movie_genre_add(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk = movie_id)
        genre_id = request.POST['genre_id']
        genre = Genre.objects.get(pk = genre_id)
        add_genre = movie.genre.add(genre)
        return redirect(f'/movie-details/{movie_id}')

def movie_genre_remove(request, movie_id, genre_id):
    genre = Genre.objects.get(pk = genre_id)
    movie = Movie.objects.get(pk = movie_id)
    genre_remove = movie.genre.remove(genre)
    return redirect(f'/movie-details/{movie_id}')

def persons(request):
    persons = Person.objects.all()
    jobs = Job.objects.all()
    message = None
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        job = Job.objects.get(pk = request.POST['job_id'])
        new_person = Person(first_name = first_name, last_name = last_name, job = job)
        new_person.save()
        message = f"Osoba {first_name} {last_name} dodana do bazy"

    return render(request, 'persons.html', {'persons': persons,'jobs': jobs, 'message': message})

def person(request, person_id):
    person = Person.objects.get(pk = person_id)
    jobs = Job.objects.all()
    message = None
    if request.method == 'POST':
        person.first_name = request.POST['first_name']
        person.last_name = request.POST['last_name']
        job = Job.objects.get(pk = request.POST['job_id'])
        person.job = job
        person.save()
        message = f"Osoba zaktualizowana"

    return render(request, 'person.html', {'person': person, 'message': message, 'jobs': jobs})

def delete_person(request, person_id):
    person = Person.objects.get(pk = person_id)
    person.delete()
    return redirect('/persons/')

def genres(request):
    genres = Genre.objects.all()
    message = None
    if request.method == 'POST':
        genre_name = request.POST['genre_name']
        new_genres = Genre.objects.create(name = genre_name)
        message = f"Gatunek {genre_name} dodady do bazy"

    return render(request, 'genres.html', {'genres': genres, 'message': message})

def delete_genre(request, genre_id):
    genre = Genre.objects.get(pk = genre_id)
    genre.delete()
    message = 'dupa'
    return redirect('/genres/')
