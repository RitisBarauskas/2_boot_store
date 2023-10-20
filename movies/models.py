from django.db.models import Model, CharField, IntegerField, DateTimeField, ManyToManyField, ForeignKey, CASCADE


class Creator(Model):
    name = CharField(max_length=256)
    key_word = CharField(max_length=256)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(Model):
    name = CharField(max_length=256)
    description = CharField(max_length=360)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=256)
    description = CharField(max_length=360)
    year = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    category = ManyToManyField(Category, through='MovieCategory')
    creator = ForeignKey(Creator, on_delete=CASCADE, related_name='movies')

    def __str__(self):
        return self.title


class MovieCategory(Model):
    movie = ForeignKey(Movie, on_delete=CASCADE)
    category = ForeignKey(Category, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.movie} - {self.category}'
