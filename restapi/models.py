from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.title} ({self.year})"

    def score(self):
        return self.rating_set.aggregate(score=models.Avg('value'))['score']

    def link(self):
        try:
            return self.link_set.get().url()
        except:
            return None

class Tag(models.Model):
    # user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='tag')
    name = models.CharField(max_length=50)
    time = models.DateTimeField()

    def __str__(self):
        return f"Tag {self.name}"

class Rating(models.Model):
    # user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    value = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return f"Rating {self.movie} - {self.value}"

class Link(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    imdb_id = models.BigIntegerField()
    tmdb_id = models.BigIntegerField()

    def __str__(self):
        return f"{self.imbd_id}"
    
    def url(self):
        return f"https://www.imdb.com/title/tt{self.imdb_id:0>7}/"