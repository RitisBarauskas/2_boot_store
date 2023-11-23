from django.db.models import Count, Q, OuterRef, Subquery
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import MovieForm, CategoryForm
from .helpers import query_debugger
from .constants import DEFAULT_COUNT_MOVIES_ON_PAGE
from .models import Movie, Category


@query_debugger
def index(request):

    filters = Q()

    subquery = Movie.objects.filter(
        year=OuterRef('year')
    ).values('year').annotate(
        count=Count('year')
    ).values('count')

    movies = Movie.objects.select_related(
        'creator',
    ).prefetch_related(
        'movie_categories__category',
    ).annotate(
        year_count=Subquery(subquery),
        category_count=Count('categories'),
    ).filter(filters).order_by('-created_at')[:DEFAULT_COUNT_MOVIES_ON_PAGE]
    return render(request, 'index.html', {'movies': movies})


@query_debugger
def movie_detail(request, movie_id):
    movie = Movie.objects.select_related(
        'creator',
    ).prefetch_related(
        'movie_categories__category',
    ).filter(
        id=movie_id,
    ).first()

    if not movie:
        raise Http404('Такого фильма нет')

    return render(request, 'movies/movie_detail.html', {'movie': movie})


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('movies:movie_detail', kwargs={'movie_id': self.object.id})


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'movies/category_form.html'
    success_url = '/'
