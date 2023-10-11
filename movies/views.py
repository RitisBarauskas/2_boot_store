from django.http import Http404
from django.shortcuts import render

from .constants import DATABASE, DEFAULT_COUNT_MOVIES_ON_PAGE


def index(request):
    movies = DATABASE.get('movies', [])
    movies = sorted(movies, key=lambda movie: movie.get('rating', 0), reverse=True)[:DEFAULT_COUNT_MOVIES_ON_PAGE]

    return render(request, 'index.html', {'movies': movies})


def movie_detail(request, movie_id):
    movies = DATABASE.get('movies', [])

    movie = next((movie for movie in movies if movie.get('id') == movie_id), None)
    if movie is None:
        raise Http404(f'Movie not found with id {movie_id}.')

    return render(request, 'movies/movie_detail.html', {'movie': movie})
