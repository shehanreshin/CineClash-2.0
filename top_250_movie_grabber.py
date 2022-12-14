import re
from random import randint
from grab import grab_top

#grabbing the top 250 movies from IMDb
movies, ratings = grab_top("http://www.imdb.com/chart/top")

#for storing movie information
movie_list = []

#extracting individual movie data
for index in range(0, len(movies)):
    movie_input = movies[index].get_text()
    movie = (' '.join(movie_input.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_input).group(1)
    data = {"movie_title": movie_title,
            "rating": ratings[index],
            "year": year}

    movie_list.append(data)
"""
# printing top 250 movies along with their ratings
for movie in movie_list:
    print(f"{movie['movie_title']} ({movie['year']}) - {float(movie['rating']):.2f}")
"""
def get_movie():
        movie = movie_list[randint(0,249)]
        print(f"{movie['movie_title']} ({movie['year']}) - {float(movie['rating']):.2f}")