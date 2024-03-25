from bs4 import BeautifulSoup
import requests
from collections import Counter

url = 'https://en.wikipedia.org/wiki/List_of_soups'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table', class_='wikitable')

#"class="wikitable sortable jquery-tablesorter"

world_titles = table.findAll("th")

rows = table.findAll('tr')

data = []

for row in rows:
    cols = row.findAll('td')
    data.append(cols)

type = [row[3] for row in data if len(row) > 3]

print(data)
# clean_titles = []

# print(clean_titles)