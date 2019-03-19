import requests
from bs4 import BeautifulSoup
import csv

intern = requests.get("https://internshala.com/internships/internship-in-bangalore").text

intern_csv = open("internshala.csv","w")
intern_writer = csv.writer(intern_csv)
intern_writer.writerow(["position","Company","link","location","stipend","start_date"])

posts = BeautifulSoup(intern, "lxml")
for post, details in zip(posts.find_all("div", class_ = "individual_internship_header"),posts.find_all("div", class_ ="individual_internship_details")):
    position = post.h4.a.text
    company = post.find(class_ = "link_display_like_text").text
    link = f"https://internshala.com/{post.h4.a['href']}"
    location = details.find(class_ = "location_link").text
    start_date = details.find(id = "start-date-first").text
    stipend = details.find(class_="stipend_container_table_cell").text
    
    company = company.strip()    
    print( position, company)
    print(link)
    print(location)
    print(start_date)
    print(stipend)
    intern_writer.writerow([position,company,link,location,stipend,start_date])

    # duration = details.find("table")
    # for d in duration.find_all("td"):
    #     #j = d.find("td")
    #     print(d['td'])
    #     print()
  
