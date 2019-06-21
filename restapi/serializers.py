from .models import Genre, Link, Movie, Rating, Tag
from rest_framework import serializers

class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'genres']

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    score = serializers.ReadOnlyField()  
    link = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = ['title', 'score', 'genres', 'link', 'year']