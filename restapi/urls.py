from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movies', views.MoviesViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('/movies/', views.movies name='movies')
]