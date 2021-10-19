from bs4 import BeautifulSoup
import requests

data = requests.get(url="https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/")
data = data.text
print(data)

soup = BeautifulSoup(data, "html.parser")

titles = soup.find_all("h3", class_="title")
titles = [title.getText() for title in titles]
titles.reverse()

with open("Day 45 - Web Scraping\movies.txt", "w", encoding="utf8") as file:
    for title in titles:
        file.write(f'{titles.index(title) + 1}) {" ".join(title.split()[1::])}\n')
