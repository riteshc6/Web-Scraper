# Hacker news scraping
from bs4 import BeautifulSoup
import requests
import csv

news_html = requests.get("https://news.ycombinator.com/news").text

news_csv = open("news.csv","w")
csv_writer = csv.writer(news_csv)
csv_writer.writerow(["Title", "Link", "Upvotes","Author"])

news = BeautifulSoup(news_html, "lxml")
#body = news.find("td", class_ = "subtext")


# head = news.find('tr', class_ = "athing")
for title, sub in zip(news.find_all(class_="athing"),news.find_all(class_ = "subtext")):
    
    headline = title.find(class_="storylink").text
    print(headline)    
    
    try :    
        link = title.find(class_="storylink")['href']
        upvotes = sub.find("span", class_ = "score").text
        author = sub.find(class_ = "hnuser").text
        print(link)
        print(upvotes, author)
        print()
        csv_writer.writerow([headline, link, upvotes, author])

    except Exception as e:
        author = None
        upvotes = None
        print("HTML page broken")
            

news_csv.close()
