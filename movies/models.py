from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import (
    Model, CharField, DateTimeField, ManyToManyField, ForeignKey, CASCADE, EmailField, UniqueConstraint,
    TextField, PositiveSmallIntegerField,
)

from .constants import (
    DEFAULT_CHARFIELD_MAX_LENGTH,
    DEFAULT_TEXTFIELD_MAX_LENGTH,
    DEFAULT_EMAILFIELD_MAX_LENGTH,
    MIN_CREATED_MOVIE_YEAR,
    MAX_CREATED_MOVIE_YEAR,
)


class TimeStampMixin(Model):
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        abstract = True


class UserModel(AbstractUser):
    email = EmailField(max_length=DEFAULT_EMAILFIELD_MAX_LENGTH, unique=True, verbose_name='Email адрес')

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.get_full_name()


class Category(TimeStampMixin, Model):
    name = CharField(max_length=DEFAULT_CHARFIELD_MAX_LENGTH, unique=True, verbose_name='Название')
    description = TextField(max_length=DEFAULT_TEXTFIELD_MAX_LENGTH, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Movie(TimeStampMixin, Model):
    title = CharField(max_length=DEFAULT_CHARFIELD_MAX_LENGTH, verbose_name='Название')
    description = TextField(max_length=DEFAULT_TEXTFIELD_MAX_LENGTH, verbose_name='Описание')
    year = PositiveSmallIntegerField(verbose_name='Год', validators=[
        MinValueValidator(MIN_CREATED_MOVIE_YEAR), MaxValueValidator(MAX_CREATED_MOVIE_YEAR)
    ])
    category = ManyToManyField(Category, through='MovieCategory', related_name='movies', verbose_name='Категория')
    creator = ForeignKey(UserModel, on_delete=CASCADE, related_name='movies', verbose_name='Кто добавил фильм в базу')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-year']

    def __str__(self):
        return self.title


class MovieCategory(Model):
    movie = ForeignKey(Movie, on_delete=CASCADE, related_name='movie_categories', verbose_name='Фильм')
    category = ForeignKey(Category, on_delete=CASCADE, related_name='movie_categories', verbose_name='Категория')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Категория фильма'
        verbose_name_plural = 'Категории фильмов'
        constraints = [
            UniqueConstraint(fields=['movie', 'category'], name='unique_movie_category'),
        ]

    def __str__(self):
        return f'{self.movie} - {self.category}'
