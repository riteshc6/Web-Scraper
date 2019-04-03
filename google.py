''' Opens all google search results'''

import requests
from bs4 import BeautifulSoup
import webbrowser, sys

print("Googling.......")

# Saving the text file search results in search
search = requests.get("https://www.google.com/search?q=" + ' '.join(sys.argv[1:])).text

# converting search into BeautifulSoup object
res = BeautifulSoup(search,"lxml")

# select all tags with class .r in a tag
find = res.select('.r a')

# Select maximum of 5 search results
numOpen = min(5, len(find))

# Open each search result in new browser
for i in range(numOpen):
    webbrowser.open('https://google.com' + find[i].get('href'))
