from django import forms
from django.forms import ModelForm

from .models import Genre, Movie, Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "job"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "job": forms.Select(attrs={"class": "form-control"}),
        }


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "director", "screenplay", "year", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "director": forms.Select(attrs={"class": "form-control"}),
            "screenplay": forms.Select(attrs={"class": "form-control"}),
            "year": forms.NumberInput(attrs={"class": "form-control"}),
            "desacription": forms.Textarea(attrs={"class": "form-control"}),
        }


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
