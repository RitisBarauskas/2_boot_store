from http import HTTPStatus

from pytest_django.asserts import assertQuerySetEqual

from movies.constants import DEFAULT_COUNT_MOVIES_ON_PAGE
from movies.models import Category, Movie
from movies.factories import MovieFactory


def test_index(db, moderator, categories, movies, moderator_client, index_url):
    """
    Тест проверки контекста на главной странице
    """
    response = moderator_client.get(index_url)
    assert response.status_code == HTTPStatus.OK
    movies = Movie.objects.order_by('-created_at')[:DEFAULT_COUNT_MOVIES_ON_PAGE]
    assert len(response.context['movies']) == len(movies)
    movie = movies[0]
    expected_movie = next((item for item in response.context['movies'] if item.id == movie.id), None)
    assert expected_movie is not None
    assert expected_movie.title == movie.title
    assert expected_movie.description == movie.description
    assert expected_movie.year == movie.year
    assert expected_movie.creator == movie.creator


def test_new_movie_first_position(db, index_url, moderator_client, categories, moderator, movies):
    """
    Тест проверки нового фильма на первой позиции.
    """
    response = moderator_client.get(index_url)
    assert response.status_code == HTTPStatus.OK
    old_movie = response.context['movies'][0]
    movie = MovieFactory(creator=moderator, categories=categories)
    response = moderator_client.get(index_url)
    assert response.status_code == HTTPStatus.OK
    assert response.context['movies'][0] == movie
    assert response.context['movies'][1] == old_movie

    movies = Movie.objects.all()
    movies_2 = Movie.objects.all()
    assertQuerySetEqual(movies, movies_2)


def test_create_category(db, client, create_category):
    """
    Тест создания категории.
    """
    old_category_ids = list(Category.objects.values_list('id', flat=True))
    data = {
        'name': 'Новая категория',
        'description': 'Описание новой категории',
    }
    response = client.post(create_category, data=data)
    assert response.status_code == 302
    new_categories = Category.objects.exclude(id__in=old_category_ids)
    assert len(new_categories) == 1
    category = new_categories[0]
    assert category.name == data['name']
    assert category.description == data['description']
