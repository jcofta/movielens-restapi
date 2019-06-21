from django.shortcuts import render
from .models import Genre, Link, Movie, Rating, Tag
from rest_framework import viewsets
from .serializers import MoviesSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer