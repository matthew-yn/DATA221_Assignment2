#Imports requests package, BeautifulSoup package from bs4, and pandas package as pd.
import requests
from bs4 import BeautifulSoup
import pandas as pd

#URL for wikipedia page.
url = "https://en.wikipedia.org/wiki/Machine_learning"
#Creates header so that website allows request.
headers = {"User-Agent": "Mozilla/5.0"}
#Downloads page.
response = requests.get(url, headers = headers)
#Converts webpage HTML into BeautifulSoup object to parse.
soup = BeautifulSoup(response.text, "html.parser")
#Finds the main content section of the page.
content = soup.find("div", id = "mw-content-text")
#Finds all table tags in content section.
tables = content.find_all("table")
#Loops through all table tags.
for table in tables:
    #Gets all rows in tables.
    rows = table.find_all("tr")
    #Checks to there are at least 3 data rows in table.
    if len(rows) < 4:
        continue
    #List to store rows of the table.
    data = []
    #Loops through data in each row and extracts it.
    for row in rows:
        cells = row.find_all(["td", "th"])

        row_data = []

        for cell in cells:
            row_data.append(cell.get_text(strip = True))

        if row_data:
            data.append(row_data)
    #Creates simple column names.
    num_cols = len(data[0])
    columns = []
    for i in range(num_cols):
        columns.append(f"col{i+1}")
    #Saves data into a DataFrame.
    df = pd.DataFrame(data, columns = columns)\
    #Converts DataFrame into CSV.
    df.to_csv("wiki_table.csv", index = False)
    #Stops program after first valid table.
    break