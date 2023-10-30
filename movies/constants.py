MOVIES = [
    {
        'id': 3,
        'name': 'The Dark Knight',
        'description': 'Some description',
        'year': 2008,
        'rating': 9.0,
        'genre': 'action',
    },
    {
        'id': 4,
        'name': 'The Godfather: Part II',
        'description': 'Some description',
        'year': 1974,
        'rating': 9.0,
        'genre': 'crime',
    },
    {
        'id': 1,
        'name': 'The Shawshank Redemption',
        'description': 'Some description',
        'year': 1994,
        'rating': 9.3,
        'genre': 'drama',
    },
    {
        'id': 2,
        'name': 'The Godfather',
        'description': 'Some description',
        'year': 1972,
        'rating': 9.2,
        'genre': 'crime',
    },
    {
        'id': 5,
        'name': 'Начало',
        'description': 'Some description',
        'year': 2010,
        'rating': 8.8,
        'genre': 'action',
    }
]

DATABASE = {
    'movies': MOVIES,
    'actors': [],
    'directors': [],
}

DEFAULT_COUNT_MOVIES_ON_PAGE = 3

DEFAULT_CHARFIELD_MAX_LENGTH = 256
DEFAULT_EMAILFIELD_MAX_LENGTH = 150
DEFAULT_TEXTFIELD_MAX_LENGTH = 980

MIN_CREATED_MOVIE_YEAR = 1900
MAX_CREATED_MOVIE_YEAR = 2025
