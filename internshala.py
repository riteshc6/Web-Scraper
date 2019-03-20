# Script to scrape Internshala.com for internships that provide the minimum amount of pay specified by the user
# All the details of internship will be saved in internshala.csv
import requests
from bs4 import BeautifulSoup
import csv
import re

# Prompt user to enter minimum stipend /month 
print("Enter Minimum Stipend :",end=" ")
min_stipend = int(input())

# Fetching HTML page of internships in Bengaluru
intern = requests.get("https://internshala.com/internships/internship-in-bangalore").text

# Initiating CSV file 
intern_csv = open("internshala.csv","w")
intern_writer = csv.writer(intern_csv)
intern_writer.writerow(["Position","Company","Location","Stipend","Start Date","Duration","Posted On","Deadline","Link"])

# Creating Beautiful Soup Object
posts = BeautifulSoup(intern, "lxml")

# Iterate over both internship details and internship header simultaneously
for post, details in zip(posts.find_all("div", class_ = "individual_internship_header"),posts.find_all("div", class_ ="individual_internship_details")):
    # Prevents the script from breaking in case any of the objects of html are missing
    try:    
        position = post.h4.a.text
        company = post.find(class_ = "link_display_like_text").text
        link = f"https://internshala.com/{post.h4.a['href']}"
        location = details.find(class_ = "location_link").text
        
        company = company.strip()    
        print( position, company)
        print(link)
        print(location)
    
        table = details.find("table")
        tr = table.find("tbody").tr
        td = tr.find_all("td")
        start_date = td[0].text.strip()
        duration =  td[1].text.strip()  
        stipend = td[2].text.strip()
        posted_on = td[3].text.strip()
        deadline = td[4].text.strip()
        print("duration :",duration)
        print(start_date)
        print(stipend)
        print(deadline)
        print()
        # Regex expression to extract out stipend amount range
        stipend_range = re.findall(r"(\d+)",stipend)     
        
        # Writes to csv files only those internships which pay minimum stipend
        if int(stipend_range[-1]) >= min_stipend :
            intern_writer.writerow([position,company,location,stipend,start_date, duration, posted_on, deadline,link])
    except Exception as e:
        print("Unpaid or missing something else")