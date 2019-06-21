from .models import Genre, Link, Movie, Rating, Tag
from rest_framework import serializers

class MoviesSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'genres']