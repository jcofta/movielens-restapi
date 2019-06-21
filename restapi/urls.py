from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movies', views.MoviesViewSet)

urlpatterns = [
    path('movies', views.movie_list, name='movie_list'),
    path('movie/<int:movieId>', views.movie, name='movie'),
    path('db', views.fetch_dataset, name='fetch'),
]