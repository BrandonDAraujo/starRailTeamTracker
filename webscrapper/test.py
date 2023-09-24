import requests
import csv
from bs4 import BeautifulSoup
 
# Making a GET request
url = 'https://game8.co/games/Honkai-Star-Rail/archives/404256'
r = requests.get(url)
 
soup = BeautifulSoup(r.text, 'html.parser')

# targets the main table in the url that contains the playable character list
body = soup.find('body')
col3 = body.find('div', class_= "l-3col")
centerCol3 = col3.find('div', class_= "l-3colMain")
mainCenterCol3 = centerCol3.find('div', class_= "l-3colMain__center l-3colMain__center--shadow")
archiveStyleWrapper = mainCenterCol3.find('div', class_ = "archive-style-wrapper")
tables = archiveStyleWrapper.find_all('table', class_= "a-table a-table a-table tablesorter")
a = tables[1].find_all('a')

count = 0
with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for line in a :
        if count % 4 == 0:
            writer.writerow([line.text, line.attrs["href"]])
        count += 1
