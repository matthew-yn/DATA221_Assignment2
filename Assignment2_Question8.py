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
#Finds the main content section of the page.
content = soup.find("div", id = "mw-content-text")

#List of headings not to be included in file.
excluded_headings = ["References", "External links", "See also", "Notes"]
#Finds all heading tags in content section.
headings = content.find_all("h2")

#Opens a file to write headings into.
with open("headings.txt", "w") as file:
    #Loops through all heading tags.
    for h2 in headings:
        #Gets heading text and removes [edit].
        heading = h2.get_text().replace("[edit]", " ").strip()
        #Checks if any headings includes excluded words.
        skip = False
        for words in excluded_headings:
            if words in heading:
                skip = True
        if skip:
            continue
        #If heading is valid, write to file.
        if heading != "":
            file.write(heading + "\n")