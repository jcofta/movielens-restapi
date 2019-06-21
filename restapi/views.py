from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Avg
from .models import Genre, Link, Movie, Rating, Tag
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieListSerializer, MovieSerializer


class MoviesViewSet(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        year = request.GET.get('year', '')
        if year:
            movies = movies.filter(year=year)
        
        sort = request.GET.get('sort', '')
        if sort:
            movies = movies.order_by(sort)
        
        tags = request.GET.getlist('tag')
        for tag in tags:
            tag_ids = Tag.objects.filter(name=tag)
            movies = movies.filter(tag__in=tag_ids)

        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie(request, movieId):
    movie = Movie.objects.get(id=movieId)
    avg_score = movie.rating_set.aggregate(score=Avg('value'))

    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data)
    
