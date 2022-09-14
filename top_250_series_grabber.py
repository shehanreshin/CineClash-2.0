from random import randint
import re
from grab import grab_top

#grabbing the top 250 series from IMDb
movies, ratings = grab_top("https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250")

#for storing series information
series_list = []

#extracting individual series data
for index in range(0, len(movies)):
    movie_input = movies[index].get_text()
    movie = (' '.join(movie_input.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_input).group(1)
    data = {"movie_title": movie_title,
            "rating": ratings[index],
            "year": year}

    series_list.append(data)
"""
# printing top 250 series along with their ratings
for series in series_list:
    print(f"{series['movie_title']} ({series['year']}) - {float(series['rating']):.2f}")
"""
def get_series():
        series = series_list[randint(0,249)]
        print(f"{series['movie_title']} ({series['year']}) - {float(series['rating']):.2f}")