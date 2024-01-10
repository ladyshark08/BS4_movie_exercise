from bs4 import BeautifulSoup

import requests

doc = open("movies.txt", "w")
target_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(target_url)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
titles = (soup.findAll("h3"))

for i in range(-1, -101, -1):
    movie_title = titles[i].text
    doc.write(f"{movie_title}\n")
