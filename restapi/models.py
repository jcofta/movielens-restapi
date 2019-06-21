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

class Tag(models.Model):
    # user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
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
    imbd_id = models.BigIntegerField()
    tmbd_id = models.BigIntegerField()

    def __str__(self):
        return f"Link {self.movie} - imbd: {self.imbd_id}, tmbd: {self.tmbd_id}"