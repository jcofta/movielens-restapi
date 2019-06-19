from django.contrib import admin
from .models import Genre, Link, Movie, Rating, Tag

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Tag)
admin.site.register(Link)
