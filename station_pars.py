import json

from bs4 import BeautifulSoup



# https://www.adam4eve.eu/info_stations.php


with open('station.html', encoding='utf-8') as f:
    html = f.read()

data = {}


soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'id': 'stations'})

q1 = table.tbody.findAll('tr', {'class': 'highlight'})


for i in q1:
    print(i.contents[1].text, i.contents[3].text)
    data[i.contents[1].text] = i.contents[3].text



table = soup.find('table', {'id': 'structures'})
q1 = table.tbody.findAll('tr', {'class': 'highlight'})


for i in q1:
    print(i.contents[1].text, i.contents[3].text)
    data[i.contents[1].text] = i.contents[3].text

with open("_stations.json", "w") as write_file:
    json.dump(data, write_file, sort_keys=False, indent=0)