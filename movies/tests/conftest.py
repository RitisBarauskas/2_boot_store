import pytest
from django.urls import reverse

from movies.factories import CategoryFactory, MovieFactory, UserFactory


@pytest.fixture
def moderator():
    return UserFactory(is_staff=True, is_superuser=True)


@pytest.fixture
def moderator_client(moderator, client):
    client.force_login(moderator)
    return client


@pytest.fixture
def categories():
    return CategoryFactory.create_batch(3)


@pytest.fixture
def movies(categories, moderator):
    return MovieFactory.create_batch(50, creator=moderator, categories=categories)


@pytest.fixture
def create_category():
    return reverse('movies:category_create')


@pytest.fixture
def create_movie():
    return reverse('movies:movie_create')


@pytest.fixture
def index_url():
    return reverse('movies:index')
