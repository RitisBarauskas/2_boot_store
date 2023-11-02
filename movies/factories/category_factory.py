import factory

from movies.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word', locale='ru_RU')
    description = factory.Faker('text', locale='ru_RU')
