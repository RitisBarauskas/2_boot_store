import factory

from movies.models import Movie


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    title = factory.Faker('word', locale='ru_RU')
    description = factory.Faker('text', locale='ru_RU')
    year = factory.Faker('year', locale='ru_RU')

    @classmethod
    def create(cls, *args, categories=None, creator=None, **kwargs):
        if not categories:
            raise ValueError('Categories is required')
        if not creator:
            raise ValueError('Creator is required')

        kwargs['creator'] = creator

        obj = super().create(**kwargs)
        obj.categories.set(categories)

        return obj