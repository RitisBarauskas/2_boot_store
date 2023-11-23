from django.test import TestCase

from django.contrib.auth import get_user_model
from django.test import Client

from movies.models import Category, Movie

User = get_user_model()


class TestMovies(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(username='user', password='12345678', email='email@email.com')
        cls.category = Category.objects.create(name='Комедии', description='Лучшие комедии')
        cls.movie = Movie.objects.create(
            title='Назад в будущее',
            description='Молодой изобретатель по имени Марти МакФлай случайно попадает в прошлое, в 1955 год. '
                        'Там он встречает своих будущих родителей, которые еще ходят в школу, и оказывает '
                        'серьезное влияние на их первое свидание. В то же время Марти должен обеспечить, '
                        'чтобы влюбленные поженились, иначе он никогда не родится.',
            year=1985,
            creator=cls.user,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")
        super().tearDownClass()

    def setUp(self) -> None:
        super().setUp()
        print("setUp")
        print('Новая авторизация...')
        self.author_client = Client()
        self.author_client.force_login(self.user)

    def tearDown(self) -> None:
        super().tearDown()
        print("tearDown")

    def test_index(self):
        print("test_index")
        movies = Movie.objects.all()
        movies_2 = Movie.objects.all()
        self.assertQuerySetEqual(movies, movies_2)


    def test_movie_detail(self):
        print("test_movie_detail")

    def test_movie_create(self):
        pass

    def test_category_create(self):
        print("test_category_create")

