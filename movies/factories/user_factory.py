import factory

from movies.models import UserModel


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModel

    username = None
    first_name = factory.Faker('first_name', locale='ru_RU')
    last_name = factory.Faker('last_name', locale='ru_RU')
    email = factory.Faker('email')
    password = factory.Faker('password')

    @classmethod
    def create(cls, *args, username=None, **kwargs):
        if not username:
            username = cls._generate_new_username()
        kwargs['username'] = username
        return super().create(**kwargs)

    @staticmethod
    def _generate_new_username():
        basename = 'testuser_'

        users_count = UserModel.objects.filter(username__startswith=basename).count()

        username = f'{basename}{users_count + 1}'

        return username
