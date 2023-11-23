from django.urls import path

from .views import index, movie_detail, MovieCreateView, CategoryCreateView


app_name = 'movies'

urlpatterns = [
    path('', index, name='index'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
]
