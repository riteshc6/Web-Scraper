# Hacker news scraping
from bs4 import BeautifulSoup
import requests
import csv

news_html = requests.get("https://news.ycombinator.com/news").text

news_csv = open("news.csv","w")
csv_writer = csv.writer(news_csv)
csv_writer.writerow(["Title", "Link"])

news = BeautifulSoup(news_html, "lxml")

#head = news.find('tr', class_ = "athing")
for title in news.find_all(class_="athing"):
    headline = title.find(class_="storylink").text
    link = title.find(class_="storylink")['href']
    print(headline)
    print(link)
    print()
    csv_writer.writerow([headline, link])

news_csv.close()
