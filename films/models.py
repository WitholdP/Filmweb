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
        return self.first_name


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
    rating = models.FloatField()
    genre = models.ManyToManyField(Genre)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=128)
