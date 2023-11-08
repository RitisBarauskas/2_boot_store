from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import render

from .helpers import query_debugger
from .constants import DEFAULT_COUNT_MOVIES_ON_PAGE
from .models import Movie


@query_debugger
def index(request):

    filters = Q()
    filters &= Q(category_count__gte=3, year__gte=2000)
    filters |= Q(category_count__gte=5, year__gte=1990, year__lte=2000)

    if request.user.is_authenticated:
        filters |= Q(creator=request.user)

    movies = Movie.objects.select_related(
        'creator',
    ).prefetch_related(
        'movie_categories__category',
    ).annotate(
        category_count=Count('categories'),
    ).filter(filters).order_by('-year')[:DEFAULT_COUNT_MOVIES_ON_PAGE]
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
