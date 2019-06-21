import requests, zipfile, io
import csv
import re
from datetime import datetime
from .models import Genre, Link, Movie, Rating, Tag

url = 'http://files.grouplens.org/datasets/movielens/ml-latest-small.zip'

def fetch():
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

    Tag.objects.all().delete()
    Rating.objects.all().delete()
    Link.objects.all().delete()
    Movie.objects.all().delete()

    with open('ml-latest-small/movies.csv', encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        for row in csvreader:
            id = row[0]
            title = row[1][:-7]
            search = re.search(r"\((\d{4})\)", row[1])
            if search:
                year = search.group(1)
            else:
                year = None
            genres = row[2].split('|')

            movie_new = Movie(
                id=id,
                title=title,
                year=year
            )
            movie_new.save()

            for genre in genres:
                if genre == '(no genres listed)':
                    break
                else:
                    try:
                        genre_obj = Genre.objects.get(name=genre)
                        if genre_obj:
                            movie_new.genres.add(genre_obj)
                    except Genre.DoesNotExist:
                        pass
    
    with open('ml-latest-small/links.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            print(row)
            movie = Movie.objects.get(id=row[0])
            imbd_id = row[1] or None
            tmbd_id = row[2] or None
            link_new = Link(
                movie=movie,
                imdb_id=imbd_id,
                tmdb_id=tmbd_id
            )
            link_new.save()

    with open('ml-latest-small/ratings.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                print(row)
                movie = Movie.objects.get(id=row[1])
                value = float(row[2])
                time = datetime.fromtimestamp(int(row[3]))

                rating_new = Rating(
                    movie=movie,
                    value=value,
                    time=time
                )

                rating_new.save()
    
    with open('ml-latest-small/tags.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                print(row)
                movie = Movie.objects.get(id=row[1])
                name = row[2]
                time = datetime.fromtimestamp(int(row[3]))

                tag_new = Tag(
                    movie=movie,
                    name=name,
                    time=time
                )

                tag_new.save()