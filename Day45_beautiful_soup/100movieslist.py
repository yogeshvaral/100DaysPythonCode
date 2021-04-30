from bs4 import BeautifulSoup
import requests


response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify())

all_the_h3_tag = soup.find_all(["props"])
print(len(all_the_h3_tag))
for tag in all_the_h3_tag:
    print(tag.getText())
