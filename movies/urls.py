from django.urls import path

from .views import index, movie_detail


app_name = 'movies'

urlpatterns = [
    path('', index, name='index'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
]
