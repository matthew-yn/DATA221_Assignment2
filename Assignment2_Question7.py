#Imports requests package and BeautifulSoup package from bs4.
import requests
from bs4 import BeautifulSoup

#URL for wikipedia page.
url = "https://en.wikipedia.org/wiki/Data_science"
#Creates header so that website allows request.
headers = {"User-Agent": "Mozilla/5.0"}
#Downloads page.
response = requests.get(url, headers = headers)
#Converts webpage HTML into BeautifulSoup object to parse.
soup = BeautifulSoup(response.text, "html.parser")

#Prints the of the page to user.
print("Title:", soup.title.text)

#Finds the main content section of the page.
content = soup.find("div", id = "mw-content-text")
#Finds all paragraph tags in content section.
paragraphs = content.find_all("p")

#Loops through all paragraph tags.
for p in paragraphs:
    #Gets the text from the paragraphs and removes all whitespaces.
    text = p.get_text().strip()
    #Checks if paragraph has at least 50 characters
    if len(text) >= 50:
        #Prints first valid paragraph found.
        print("\nFirst paragraph:")
        print(text)
        #Stops printing after valid paragraph is found.
        break