from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from random import randint

def grab_top(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    movies = soup.select('td.titleColumn')
    ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]
    return movies, ratings
