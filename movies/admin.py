from django.contrib import admin

from .models import Movie, Category, MovieCategory, UserModel

admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(MovieCategory)
admin.site.register(UserModel)
