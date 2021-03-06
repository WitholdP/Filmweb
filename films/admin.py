from django.contrib import admin

from .models import Genre, Job, Movie, Person

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Genre)
admin.site.register(Job)
