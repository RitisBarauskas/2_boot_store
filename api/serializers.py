from rest_framework import serializers

from movies.models import Movie, Category, MovieCategory


class MovieShortReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title')


class CategoryReadSerializer(serializers.ModelSerializer):
    movies = MovieShortReadSerializer(many=True, read_only=True)
    movies_count = serializers.IntegerField(source='movies.count', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'movies', 'movies_count')


class MovieReadSerializer(serializers.ModelSerializer):
    categories = CategoryReadSerializer(many=True, read_only=True)
    creator = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'year', 'categories', 'creator')


class CategoryInMovieSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = MovieCategory
        fields = ('id',)


class MovieWriteSerializer(serializers.ModelSerializer):
    categories = CategoryInMovieSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'year', 'categories')

    def validate_year(self, value):
        if value < 1900 or value > 2021:
            raise serializers.ValidationError('Год должен быть в диапазоне от 1900 до 2021')
        return value

    def validate_categories(self, value):
        if len(value) > 3:
            raise serializers.ValidationError('Количество категорий не должно превышать 3')
        return value

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        movie = Movie.objects.create(
            creator=self.context['request'].user,
            **validated_data,
        )
        for category_data in categories_data:
            MovieCategory.objects.create(movie=movie, category=category_data['id'])
        return movie

    def to_representation(self, instance):
        return MovieReadSerializer(instance).data


class CategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
