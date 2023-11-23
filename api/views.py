from rest_framework.viewsets import ModelViewSet

from movies.models import Movie, Category
from .serializers import MovieReadSerializer, CategoryReadSerializer, MovieWriteSerializer, CategoryWriteSerializer


class MovieViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MovieWriteSerializer
        return MovieReadSerializer

    def get_queryset(self):
        return Movie.objects.prefetch_related('categories').order_by('-id')


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CategoryWriteSerializer
        return CategoryReadSerializer
