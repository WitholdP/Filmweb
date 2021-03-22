from django.conf import settings
from django.db import models


class Job(models.Model):
    job_name = models.CharField(max_length=32)

    def __str__(self):
        return self.job_name


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, default=4)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="director"
    )
    screenplay = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="screenplay"
    )
    starring = models.ManyToManyField(Person, through="PersonMovie")
    year = models.IntegerField()
    genre = models.ManyToManyField(Genre)
    description = models.TextField(null=True)
    cover = models.FileField(upload_to="covers", null=True)

    def __str__(self):
        return self.title


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=128)


class MRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(null=True)
    posting_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
