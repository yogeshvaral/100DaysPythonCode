from bs4 import BeautifulSoup
import requests

with open("website.html", encoding='utf8') as file:
    content = file.read()
    # print(content)

soup = BeautifulSoup(content,"html.parser")
print(soup.title)

all_the_anchor_tag = soup.find_all(name="a")

print(all_the_anchor_tag)

for tag in all_the_anchor_tag:
    print(tag.getText())
    print(tag.get("href"))

#
# h3_heading = soup.find_all("h3",class="heading")
# print(h3_heading)

name = soup.select_one("#name")
print(name)
# headings = soup.setup(".heading")
# print(headings)



response = requests.get(url="https://news.ycombinator.com/")
# print(response.text)

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")
print(soup.title)
articles = soup.find_all(name="a",class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text= article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_uplvotes = [ int(score.getText().split(" ")[0]) for score in soup.find_all(name="span",class_="score")]

print(article_texts)
print(article_links)
print(article_uplvotes)
print(max(article_uplvotes))
largest_index =  article_uplvotes.index(max(article_uplvotes))
print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])