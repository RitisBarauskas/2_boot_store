from random import choice, choices, randint

from django.core.management import BaseCommand
from django.db import transaction

from movies.factories import UserFactory, CategoryFactory, MovieFactory


class Command(BaseCommand):
    help = 'Создание данных на основе фабрик'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Начинаем создание данных'))

        self.stdout.write(self.style.SUCCESS('Создание пользователей'))
        users = UserFactory.create_batch(10)

        self.stdout.write(self.style.SUCCESS('Создание категорий'))
        categories = []
        for _ in range(20):
            try:
                category = CategoryFactory.create()
            except Exception:
                continue
            categories.append(category)

        self.stdout.write(self.style.SUCCESS('Создание фильмов'))
        movies = []
        for _ in range(100):
            movie = MovieFactory.create(
                categories=choices(categories, k=randint(2, 5)),
                creator=choice(users)
            )
            movies.append(movie)

        self.stdout.write(self.style.SUCCESS(f'Создано {len(users)} пользователей'))
        self.stdout.write(self.style.SUCCESS(f'Создано {len(categories)} категорий'))
        self.stdout.write(self.style.SUCCESS(f'Создано {len(movies)} фильмов'))

        self.stdout.write(self.style.SUCCESS('Данные успешно созданы'))
