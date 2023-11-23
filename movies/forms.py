from django.forms import ModelForm

from .models import Movie, Category


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'year', 'categories']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
