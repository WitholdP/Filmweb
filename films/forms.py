from django import forms
from django.forms import ModelForm

from .models import Movie, Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "job"]


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
